import json

# 50 Python Q&A pairs
dataset = [
    # Basic Operations
    {"instruction": "How to add two numbers in Python?", "input": "",
     "output": "```python\ndef add(a, b):\n    return a + b\n\n# Example\nresult = add(5, 3)\nprint(result)  # Output: 8\n```\n\nThis function takes two parameters and returns their sum using the + operator."},

    {"instruction": "How to subtract two numbers in Python?", "input": "",
     "output": "```python\ndef subtract(a, b):\n    return a - b\n\n# Example\nresult = subtract(10, 4)\nprint(result)  # Output: 6\n```\n\nThis function subtracts the second parameter from the first."},

    {"instruction": "How to multiply two numbers in Python?", "input": "",
     "output": "```python\ndef multiply(a, b):\n    return a * b\n\n# Example\nresult = multiply(4, 5)\nprint(result)  # Output: 20\n```\n\nThis function multiplies two numbers using the * operator."},

    {"instruction": "How to divide two numbers in Python?", "input": "",
     "output": "```python\ndef divide(a, b):\n    if b == 0:\n        return \"Error: Division by zero\"\n    return a / b\n\n# Example\nresult = divide(10, 2)\nprint(result)  # Output: 5.0\n```\n\nThis function divides two numbers and handles division by zero."},

    # Strings
    {"instruction": "How to reverse a string in Python?", "input": "",
     "output": "```python\ndef reverse_string(s):\n    return s[::-1]\n\n# Example\nprint(reverse_string('hello'))  # Output: 'olleh'\n```\n\nThis uses slice notation with step -1 to reverse the string."},

    {"instruction": "How to check if a string is palindrome in Python?", "input": "",
     "output": "```python\ndef is_palindrome(s):\n    return s == s[::-1]\n\n# Example\nprint(is_palindrome('racecar'))  # Output: True\nprint(is_palindrome('hello'))    # Output: False\n```\n\nThis compares the string with its reverse."},

    {"instruction": "How to count vowels in a string in Python?", "input": "",
     "output": "```python\ndef count_vowels(s):\n    vowels = 'aeiouAEIOU'\n    return sum(1 for char in s if char in vowels)\n\n# Example\nprint(count_vowels('hello'))  # Output: 2\n```\n\nThis counts characters that are in the vowel set."},

    {"instruction": "How to convert string to uppercase in Python?", "input": "",
     "output": "```python\ndef to_uppercase(s):\n    return s.upper()\n\n# Example\nprint(to_uppercase('hello'))  # Output: 'HELLO'\n```\n\nUses the built-in upper() method."},

    {"instruction": "How to convert string to lowercase in Python?", "input": "",
     "output": "```python\ndef to_lowercase(s):\n    return s.lower()\n\n# Example\nprint(to_lowercase('HELLO'))  # Output: 'hello'\n```\n\nUses the built-in lower() method."},

    {"instruction": "How to remove spaces from a string in Python?", "input": "",
     "output": "```python\ndef remove_spaces(s):\n    return s.replace(\" \", \"\")\n\n# Example\nprint(remove_spaces('hello world'))  # Output: 'helloworld'\n```\n\nUses replace() to remove all spaces."},

    # Lists
    {"instruction": "How to sort a list in Python?", "input": "",
     "output": "```python\nnumbers = [5, 2, 8, 1, 9]\nnumbers.sort()\nprint(numbers)  # Output: [1, 2, 5, 8, 9]\n\n# Or sorted() for a new list\nnew_list = sorted([5, 2, 8, 1, 9])\nprint(new_list)  # Output: [1, 2, 5, 8, 9]\n```\n\nsort() modifies the original list. sorted() returns a new list."},

    {"instruction": "How to reverse a list in Python?", "input": "",
     "output": "```python\ndef reverse_list(lst):\n    return lst[::-1]\n\n# Example\nprint(reverse_list([1, 2, 3, 4]))  # Output: [4, 3, 2, 1]\n```\n\nUses slice notation to reverse the list."},

    {"instruction": "How to find max in a list in Python?", "input": "",
     "output": "```python\ndef find_max(lst):\n    return max(lst)\n\n# Example\nprint(find_max([3, 7, 2, 9, 5]))  # Output: 9\n```\n\nUses the built-in max() function."},

    {"instruction": "How to find min in a list in Python?", "input": "",
     "output": "```python\ndef find_min(lst):\n    return min(lst)\n\n# Example\nprint(find_min([3, 7, 2, 9, 5]))  # Output: 2\n```\n\nUses the built-in min() function."},

    {"instruction": "How to sum all elements in a list in Python?", "input": "",
     "output": "```python\ndef sum_list(lst):\n    return sum(lst)\n\n# Example\nprint(sum_list([1, 2, 3, 4, 5]))  # Output: 15\n```\n\nUses the built-in sum() function."},

    {"instruction": "How to remove duplicates from a list in Python?", "input": "",
     "output": "```python\ndef remove_duplicates(lst):\n    return list(set(lst))\n\n# Example\nprint(remove_duplicates([1, 2, 2, 3, 3, 4]))  # Output: [1, 2, 3, 4]\n```\n\nConverts to set to remove duplicates, then back to list."},

    {"instruction": "How to find even numbers in a list in Python?", "input": "",
     "output": "```python\ndef get_even_numbers(lst):\n    return [x for x in lst if x % 2 == 0]\n\n# Example\nprint(get_even_numbers([1, 2, 3, 4, 5, 6]))  # Output: [2, 4, 6]\n```\n\nUses list comprehension with modulo operator."},

    {"instruction": "How to find odd numbers in a list in Python?", "input": "",
     "output": "```python\ndef get_odd_numbers(lst):\n    return [x for x in lst if x % 2 != 0]\n\n# Example\nprint(get_odd_numbers([1, 2, 3, 4, 5, 6]))  # Output: [1, 3, 5]\n```\n\nUses list comprehension with modulo operator."},

    # Dictionaries
    {"instruction": "How to create a dictionary in Python?", "input": "",
     "output": "```python\n# Empty dictionary\nmy_dict = {}\n\n# With values\nperson = {\n    \"name\": \"John\",\n    \"age\": 30,\n    \"city\": \"New York\"\n}\n\n# Accessing values\nprint(person[\"name\"])  # Output: John\n```\n\nDictionaries store key-value pairs."},

    {"instruction": "How to iterate over a dictionary in Python?", "input": "",
     "output": "```python\nperson = {\n    \"name\": \"John\",\n    \"age\": 30,\n    \"city\": \"New York\"\n}\n\n# Iterate over keys and values\nfor key, value in person.items():\n    print(f\"{key}: {value}\")\n```\n\nUses items() to get key-value pairs."},

    {"instruction": "How to merge two dictionaries in Python?", "input": "",
     "output": "```python\ndict1 = {\"a\": 1, \"b\": 2}\ndict2 = {\"c\": 3, \"d\": 4}\n\nmerged = {**dict1, **dict2}\nprint(merged)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}\n```\n\nUses dictionary unpacking to merge."},

    # Conditionals
    {"instruction": "How to check if number is even or odd in Python?", "input": "",
     "output": "```python\ndef check_even_odd(n):\n    if n % 2 == 0:\n        return \"Even\"\n    else:\n        return \"Odd\"\n\n# Example\nprint(check_even_odd(7))  # Output: Odd\n```\n\nUses modulo operator to check divisibility by 2."},

    {"instruction": "How to check if number is prime in Python?", "input": "",
     "output": "```python\ndef is_prime(n):\n    if n <= 1:\n        return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:\n            return False\n    return True\n\n# Example\nprint(is_prime(7))   # Output: True\nprint(is_prime(10))  # Output: False\n```\n\nChecks divisibility up to square root of n."},

    {"instruction": "How to find largest of three numbers in Python?", "input": "",
     "output": "```python\ndef largest_of_three(a, b, c):\n    return max(a, b, c)\n\n# Example\nprint(largest_of_three(10, 25, 15))  # Output: 25\n```\n\nUses the built-in max() function."},

    {"instruction": "How to check leap year in Python?", "input": "",
     "output": "```python\ndef is_leap_year(year):\n    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\n\n# Example\nprint(is_leap_year(2020))  # Output: True\nprint(is_leap_year(2021))  # Output: False\n```\n\nChecks leap year conditions."},

    # Loops
    {"instruction": "How to print numbers from 1 to 10 in Python?", "input": "",
     "output": "```python\n# Using for loop\nfor i in range(1, 11):\n    print(i)\n```\n\nrange(1, 11) generates numbers from 1 to 10."},

    {"instruction": "How to print a pattern in Python?", "input": "",
     "output": "```python\ndef print_pattern(n):\n    for i in range(1, n + 1):\n        print('*' * i)\n\n# Example\nprint_pattern(5)\n```\n\nPrints a triangle pattern with n rows."},

    # Functions
    {"instruction": "How to create a function in Python?", "input": "",
     "output": "```python\ndef greet(name):\n    return f\"Hello, {name}!\"\n\n# Example\nprint(greet(\"Alice\"))  # Output: Hello, Alice!\n```\n\nFunctions defined with def keyword."},

    {"instruction": "How to create a function with default parameters in Python?", "input": "",
     "output": "```python\ndef greet(name=\"World\"):\n    return f\"Hello, {name}!\"\n\n# Example\nprint(greet())       # Output: Hello, World!\nprint(greet(\"Alice\")) # Output: Hello, Alice!\n```\n\nDefault parameters provide fallback values."},

    {"instruction": "How to create a lambda function in Python?", "input": "",
     "output": "```python\n# Lambda function for squaring\nsquare = lambda x: x ** 2\n\n# Example\nprint(square(5))  # Output: 25\n```\n\nLambda creates anonymous functions."},

    {"instruction": "How to use map function in Python?", "input": "",
     "output": "```python\nnumbers = [1, 2, 3, 4, 5]\nsquared = list(map(lambda x: x**2, numbers))\nprint(squared)  # Output: [1, 4, 9, 16, 25]\n```\n\nmap() applies a function to every element."},

    {"instruction": "How to use filter function in Python?", "input": "",
     "output": "```python\nnumbers = [1, 2, 3, 4, 5, 6]\nevens = list(filter(lambda x: x % 2 == 0, numbers))\nprint(evens)  # Output: [2, 4, 6]\n```\n\nfilter() selects elements that match a condition."},

    # Classes
    {"instruction": "How to create a class in Python?", "input": "",
     "output": "```python\nclass Person:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n    \n    def greet(self):\n        return f\"Hello, I'm {self.name}\"\n\n# Example\np = Person(\"Alice\", 25)\nprint(p.greet())  # Output: Hello, I'm Alice\n```\n\nClasses define object blueprints."},

    {"instruction": "How to create a class with inheritance in Python?", "input": "",
     "output": "```python\nclass Animal:\n    def __init__(self, name):\n        self.name = name\n    \n    def speak(self):\n        return \"Some sound\"\n\nclass Dog(Animal):\n    def speak(self):\n        return \"Woof!\"\n\n# Example\nd = Dog(\"Buddy\")\nprint(d.speak())  # Output: Woof!\n```\n\nInheritance lets child class reuse parent methods."},

    # File handling
    {"instruction": "How to read a file in Python?", "input": "",
     "output": "```python\nwith open('file.txt', 'r') as file:\n    content = file.read()\n    print(content)\n```\n\nUses with statement for automatic file closing."},

    {"instruction": "How to write to a file in Python?", "input": "",
     "output": "```python\nwith open('file.txt', 'w') as file:\n    file.write('Hello, World!')\n```\n\nUses 'w' mode to write to file."},

    # Algorithms
    {"instruction": "How to implement binary search in Python?", "input": "",
     "output": "```python\ndef binary_search(arr, target):\n    left, right = 0, len(arr) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1\n\n# Example\narr = [1, 2, 3, 4, 5]\nprint(binary_search(arr, 3))  # Output: 2\n```\n\nBinary search divides array in half each step."},

    {"instruction": "How to implement bubble sort in Python?", "input": "",
     "output": "```python\ndef bubble_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(0, n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n    return arr\n\n# Example\nprint(bubble_sort([64, 34, 25, 12, 22]))  # Output: [12, 22, 25, 34, 64]\n```\n\nBubble sort repeatedly swaps adjacent elements."},

    {"instruction": "How to implement selection sort in Python?", "input": "",
     "output": "```python\ndef selection_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        min_idx = i\n        for j in range(i+1, n):\n            if arr[j] < arr[min_idx]:\n                min_idx = j\n        arr[i], arr[min_idx] = arr[min_idx], arr[i]\n    return arr\n\n# Example\nprint(selection_sort([64, 34, 25, 12, 22]))  # Output: [12, 22, 25, 34, 64]\n```\n\nSelection sort finds minimum element and swaps."},

    {"instruction": "How to implement insertion sort in Python?", "input": "",
     "output": "```python\ndef insertion_sort(arr):\n    for i in range(1, len(arr)):\n        key = arr[i]\n        j = i-1\n        while j >= 0 and arr[j] > key:\n            arr[j+1] = arr[j]\n            j -= 1\n        arr[j+1] = key\n    return arr\n\n# Example\nprint(insertion_sort([64, 34, 25, 12, 22]))  # Output: [12, 22, 25, 34, 64]\n```\n\nInsertion sort inserts elements into sorted position."},

    # Misc
    {"instruction": "How to generate random numbers in Python?", "input": "",
     "output": "```python\nimport random\n\n# Random integer\nprint(random.randint(1, 100))  # Output: random number between 1-100\n\n# Random float\nprint(random.random())  # Output: random number between 0-1\n```\n\nUses random module for random number generation."},

    {"instruction": "How to get current date in Python?", "input": "",
     "output": "```python\nfrom datetime import datetime\n\nnow = datetime.now()\nprint(now)  # Output: current date and time\nprint(now.strftime(\"%Y-%m-%d\"))  # Output: YYYY-MM-DD\n```\n\nUses datetime module for date operations."},

    {"instruction": "How to calculate square root in Python?", "input": "",
     "output": "```python\nimport math\n\ndef sqrt(n):\n    return math.sqrt(n)\n\n# Example\nprint(sqrt(16))  # Output: 4.0\n```\n\nUses math.sqrt() for square root calculation."},

    {"instruction": "How to handle errors in Python?", "input": "",
     "output": "```python\ndef safe_divide(a, b):\n    try:\n        return a / b\n    except ZeroDivisionError:\n        return \"Error: Cannot divide by zero\"\n\n# Example\nprint(safe_divide(10, 2))  # Output: 5.0\nprint(safe_divide(10, 0))  # Output: Error: Cannot divide by zero\n```\n\nUses try-except to handle errors."},

    {"instruction": "How to create a list comprehension in Python?", "input": "",
     "output": "```python\n# Square numbers\nsquares = [x**2 for x in range(1, 6)]\nprint(squares)  # Output: [1, 4, 9, 16, 25]\n\n# Filter even numbers\nevens = [x for x in range(1, 11) if x % 2 == 0]\nprint(evens)  # Output: [2, 4, 6, 8, 10]\n```\n\nList comprehensions create lists elegantly."},

    {"instruction": "How to use enumerate in Python?", "input": "",
     "output": "```python\nfruits = ['apple', 'banana', 'cherry']\nfor index, fruit in enumerate(fruits):\n    print(f\"{index}: {fruit}\")\n```\n\nenumerate() adds counter to iterables."},

    {"instruction": "How to use zip in Python?", "input": "",
     "output": "```python\nnames = ['Alice', 'Bob', 'Charlie']\nages = [25, 30, 35]\n\nfor name, age in zip(names, ages):\n    print(f\"{name}: {age}\")\n```\n\nzip() aggregates elements from multiple iterables."},

    {"instruction": "How to use any/all in Python?", "input": "",
     "output": "```python\nnumbers = [1, 2, 3, 4, 5]\n\nprint(any(x > 4 for x in numbers))  # Output: True\nprint(all(x > 0 for x in numbers))  # Output: True\nprint(all(x > 5 for x in numbers))  # Output: False\n```\n\nany() checks if any element is True. all() checks if all are True."},

    {"instruction": "How to sort a dictionary by value in Python?", "input": "",
     "output": "```python\nperson = {'Alice': 25, 'Bob': 30, 'Charlie': 35}\nsorted_person = dict(sorted(person.items(), key=lambda x: x[1]))\nprint(sorted_person)  # Output: {'Alice': 25, 'Bob': 30, 'Charlie': 35}\n```\n\nUses sorted() with lambda to sort by value."},

    {"instruction": "How to create a list of random numbers in Python?", "input": "",
     "output": "```python\nimport random\n\ndef random_list(n):\n    return [random.randint(1, 100) for _ in range(n)]\n\n# Example\nprint(random_list(5))  # Output: [random numbers]\n```\n\nCombines random module with list comprehension."},

    {"instruction": "How to find factorial using math module in Python?", "input": "",
     "output": "```python\nimport math\n\ndef factorial(n):\n    return math.factorial(n)\n\n# Example\nprint(factorial(5))  # Output: 120\n```\n\nUses math.factorial() for fast factorial computation."},
]

# Save to JSON file
with open('dataset.jsonl', 'w') as f:
    for item in dataset:
        f.write(json.dumps(item) + '\n')

print(f"✅ Dataset created with {len(dataset)} examples")
print("📁 Saved as 'dataset.jsonl'")