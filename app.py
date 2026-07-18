import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
import os

# Page config
st.set_page_config(page_title="CodeBot", page_icon="")

# Get absolute path to codebot_lora folder
LORA_PATH = os.path.join(os.getcwd(), "codebot_lora")


# Load model
@st.cache_resource
def load_model():
    # Check if folder exists
    if not os.path.exists(LORA_PATH):
        raise FileNotFoundError(f"Folder not found: {LORA_PATH}")

    # Load base model
    base_model = AutoModelForCausalLM.from_pretrained(
        "unsloth/Qwen2.5-0.5B",
        torch_dtype=torch.float16,
        device_map="auto",
    )

    # Load LoRA adapters
    model = PeftModel.from_pretrained(base_model, LORA_PATH)
    tokenizer = AutoTokenizer.from_pretrained(LORA_PATH)

    return model, tokenizer


try:
    model, tokenizer = load_model()
    model_loaded = True
except Exception as e:
    model_loaded = False
    st.error(f"Model not found. Error: {str(e)}")

# Sidebar
with st.sidebar:
    st.header("Settings")
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    st.divider()
    st.caption("Fine-tuned on 51 Python examples")
    if model_loaded:
        st.success("Model loaded")
    else:
        st.error("Model not loaded")
    st.divider()
    st.caption("Mohsin Yahya Fine Tuning")

# Title
st.title("CodeBot")
st.caption("Python code generation assistant")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me to write Python code..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        if model_loaded:
            # Generate response
            inputs = tokenizer(
                f"### Instruction:\n{prompt}\n\n### Response:\n",
                return_tensors="pt",
            ).to("cuda" if torch.cuda.is_available() else "cpu")

            outputs = model.generate(
                **inputs,
                max_new_tokens=300,
                temperature=0.3,
                do_sample=True,
            )

            response = tokenizer.decode(outputs[0], skip_special_tokens=True)
            # Extract only the response part
            if "### Response:" in response:
                response = response.split("### Response:")[-1].strip()

            st.markdown(response)
        else:
            st.error("Model not loaded. Please check the codebot_lora folder.")
            response = "Model not available"

    st.session_state.messages.append({"role": "assistant", "content": response})