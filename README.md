# VeriLLM — LLM-Assisted Static Code Analyzer

VeriLLM is an AI-assisted static code analysis prototype that analyzes source code using Large Language Models (LLMs) to identify:

* Possible bugs
* Security vulnerabilities
* Performance inefficiencies
* Code quality issues
* Complexity insights
* Improvement suggestions

The project explores the intersection of:

* Software Verification
* Static Program Analysis
* AI-Assisted Developer Tooling
* Automated Reasoning

Inspired by modern research in programming languages and software foundations.

---

# Features

* AI-powered code analysis
* Static reasoning workflow
* Security issue detection
* Complexity analysis
* Performance suggestions
* Clean responsive UI
* Flask-based backend
* Gemini API integration

---

# Tech Stack

## Frontend

* HTML
* CSS

## Backend

* Python
* Flask

## AI Integration

* Google Gemini API

---

# Project Structure

```bash
VeriLLM/
│
├── app.py
├── requirements.txt
├── .env
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Saqib-Uzair/veriLLM.git
cd veriLLM
```

---

## Create Virtual Environment

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

Get API key from:

https://aistudio.google.com/app/apikey

---

# Run The Application

```bash
python app.py
```

Open browser:

```txt
http://127.0.0.1:5000
```

---

# Example Test Input

```python
def divide(a, b):
    return a / b

x = divide(10, 0)
print(x)
```

---

# Future Improvements

* AST-based analysis
* Control Flow Graph (CFG) generation
* Symbolic execution
* Multi-language support
* Concurrency risk detection
* LLVM integration
* AI-assisted verification workflows

---

# Research Motivation

This project explores how Large Language Models can assist in:

* Automated code reasoning
* Static program analysis
* Software verification workflows
* AI-assisted debugging

The long-term vision is to investigate hybrid approaches combining:

* Formal reasoning
* Static analysis
* Generative AI systems

---

# License

This project is open-source and available under the MIT License.
