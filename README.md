# ChatGPT API Python Integration

This repository contains a Python implementation that integrates the [OpenAI ChatGPT API](https://platform.openai.com/docs/guides/text-generation) for creating a simple interactive question-and-answer assistant.

## Overview

The Python script interacts with the ChatGPT API to provide real-time responses to user queries while maintaining the context of the conversation. It allows users to ask questions, receive answers, and continue the conversation in a natural flow.

### Key Features
- **API Integration:** Easy setup using the OpenAI API key.
- **Message History Management:** Maintains context of interactions for more accurate responses.
- **Continuous Interaction:** Allows ongoing conversations until the user decides to stop.

## Setup

### Prerequisites
1. **Python >= 3.11 installed on your machine.
2. **OpenAI API Key:** You need an API key from [OpenAI](https://platform.openai.com/settings/organization/api-keys).

### Installation

1. Install the required dependencies:
    ```bash
    pip install openai
    ```

2. Replace the API key in the script (`API_ChatGPT.py`) with your own.

3. Run the script:
    ```bash
    python3 API_ChatGPT.py
    ```

### Example Usage

Once the script is running, you can input your question in the terminal. The assistant will respond based on the message history, and you can continue the conversation until you type `'end'` to stop.

```bash
Ask your question: Who was Carl Sagan?
Answer: Carl Sagan was an American astronomer, astrophysicist, and science communicator.
Ask your question: Tell me more about his work.
Answer: Carl Sagan made significant contributions to our understanding of planetary science...
