CodeBot - Python Code Generation Assistant
CodeBot is a fine-tuned code generation assistant built using Qwen2.5-0.5B with LoRA (Low-Rank Adaptation) fine-tuning. It generates Python code snippets in response to natural language queries.

Features
Generates Python code from natural language prompts

Fine-tuned on 51 Python Q&A examples covering basic to intermediate concepts

Clean and minimal Streamlit web interface

Lightweight and runs locally

Technology Stack
Component	Technology
Base Model	Qwen2.5-0.5B
Fine-tuning Method	LoRA (Low-Rank Adaptation)
Framework	Unsloth, Transformers, PEFT
UI Framework	Streamlit
Backend	PyTorch
Dataset Overview

The model was fine-tuned on 51 Python Q&A pairs covering:

Basic operations (add, subtract, multiply, divide)

String manipulation (reverse, palindrome, case conversion)

List operations (sort, reverse, min, max, sum)

Dictionary operations (create, iterate, merge)

Conditionals and loops

Functions and lambda expressions

Classes and inheritance

File handling

Common algorithms (binary search, bubble sort, selection sort)

Sample Queries
How to add two numbers in Python?

Write a function to reverse a string

Create a class called Person

How to sort a list in Python?

Calculate factorial of a number

Project Structure
text
codebot/
├── app.py                    # Streamlit UI application
├── dataset.jsonl             # Training dataset (51 examples)
├── generate_dataset.py       # Dataset generation script
├── codebot_lora/             # Fine-tuned LoRA adapters
│   ├── adapter_config.json
│   ├── adapter_model.safetensors
│   └── tokenizer files
└── .venv/                    # Python virtual environment

Setup Instructions : 
Clone the repository

Create a virtual environment:

bash
python -m venv .venv
Activate the environment:

bash
.venv\Scripts\activate
Install dependencies:

bash
pip install -r requirements.txt
Run the application:

bash
streamlit run app.py

Requirements
text
streamlit
torch
transformers
peft
accelerate

How It Works
User enters a natural language query

Query is formatted with instruction template

Fine-tuned Qwen2.5-0.5B model generates a response

Response is extracted and displayed in the chat interface

Fine-Tuning Details
Base Model: unsloth/Qwen2.5-0.5B

LoRA Rank: 16

Training Steps: 60

Learning Rate: 2e-4

Batch Size: 4

Gradient Accumulation Steps: 4

Quantization: 4-bit (QLoRA)

Loss at completion: 0.97

Future Improvements
Expand dataset with more diverse examples

Increase training steps for better accuracy

Add support for multiple programming languages

Deploy as a web service

Add code execution capability

Author
Mohsin Yahya 

License
This project is for educational and personal use.

Acknowledgments
Unsloth team for the fine-tuning framework
Qwen team for the base model

Hugging Face for Transformers and PEFT libraries
