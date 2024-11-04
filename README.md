# LangChain Output Parsers

This repository contains two Python programs that leverage the LangChain framework for interacting with language models, each designed with a different approach to handling output parsing. The goal of these programs is to demonstrate flexible output parsing techniques using LangChain's powerful chaining and output parsing capabilities.

## Table of Contents
- [Overview](#overview)
- [Getting Started](#getting-started)
- [Programs](#programs)
  - [main_output_parsers_1.py](#main_output_parsers_1py)
  - [main_output_parsers_json_output_2.py](#main_output_parsers_json_output_2py)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)



## Overview

LangChain provides a modular way to build applications with Large Language Models (LLMs) by allowing the construction of chains that combine models, prompts, and parsers. This repository contains examples demonstrating two output parsing strategies with LangChain:
1. Parsing output with expected results provided in the prompt.
2. Parsing output in a structured JSON format using LangChain's `StructuredOutputParser`.

## Getting Started

To run these programs, clone this repository and install the dependencies as described below. Each script demonstrates a different approach to obtaining structured output from the LLM.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vinodvpillai/langchain-output-parsers.git
   cd langchain-output-parsers
   ```

2. **Install dependencies:**
   Ensure you have the required dependencies installed (see [Dependencies](#dependencies)).

3. **Run the scripts:**
   - `main_output_parsers_1.py` – This script demonstrates basic output parsing by passing expected output directly as part of the prompt.
   - `main_output_parsers_json_output_2.py` – This script parses the response into a JSON format using `StructuredOutputParser` for more structured data extraction.

## Programs

### main_output_parsers_1.py

This script demonstrates a simple approach to parsing outputs by providing the expected format within the prompt itself. Here, the expected structure of the output is embedded in the prompt, guiding the model to produce a response that aligns closely with our expectations.

- **Use Case:** Ideal when working with simpler data or when minor deviations from the expected output format are acceptable.
- **LangChain Components Used:** Basic prompt chaining without explicit structured parsing.
- **Example Usage:**
  ```python
  python main_output_parsers_1.py
  ```

### main_output_parsers_json_output_2.py

This script takes advantage of LangChain’s `StructuredOutputParser` to parse the output explicitly into JSON format. The `StructuredOutputParser` allows for structured responses by specifying the output schema beforehand, enabling the program to capture well-formed JSON data for downstream processing.

- **Use Case:** Recommended for scenarios requiring strict adherence to structured data formats (e.g., JSON), making it easy to work with the parsed data programmatically.
- **LangChain Components Used:** `StructuredOutputParser` for defining and parsing the JSON output schema.
- **Example Usage:**
  ```python
  python main_output_parsers_json_output_2.py
  ```

## Dependencies

To install the required dependencies, use:
```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! If you'd like to add new features or fix bugs, please fork this repository and submit a pull request.

## License

This project is licensed under the MIT License.

