# AI Medical Chatbot 2.0 (with Vision and Voice)

A simple Python script that uses the Groq API and a multimodal LLM to analyze images
## Features

- Encodes images to base64 format
- Queries a multimodal LLM (meta-llama/llama-4-maverick-17b-128e-instruct)
- Prints the analysis result

## Requirements

- Python 3.13
- Pipenv (for dependency management)
- GROQ_API_KEY environment variable set

## Installation

1. Clone the repository:
   ```
   git clone <your-repo-url>
   cd ai_voicebot
   ```

2. Install dependencies:
   ```
   pipenv install
   ```

3. Set your GROQ API key:
   ```
   export GROQ_API_KEY=your_api_key_here
   ```

## Usage

1. Place your image file (e.g., `acne.jpg`) in the project directory.

2. Run the script:
   ```
   pipenv run python brain_of_doctor.py
   ```

The script will analyze the image and print the skin condition description.

## Files

- `brain_of_doctor.py`: Main script
- `Pipfile`: Dependency specification
- `Pipfile.lock`: Locked dependencies
- `.gitignore`: Ignored files
