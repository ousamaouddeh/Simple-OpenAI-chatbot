# Simple OpenAI Chatbot

A minimal command-line chatbot built with Python and the OpenAI API. It keeps track of conversation history and lets you chat with an AI assistant directly from your terminal.

## Features

- Simple CLI chat loop
- Maintains conversation context across turns
- Configurable system prompt (currently set to a sassy, fed-up assistant persona)
- Environment-based API key management via `.env`

## Requirements

- Python 3.9+
- An OpenAI API key ([get one here](https://platform.openai.com/api-keys))

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ousamaouddeh/Simple-OpenAI-chatbot.git
   cd Simple-OpenAI-chatbot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the chatbot:
```bash
python main.py
```

Type your message and press Enter to chat. Type `exit` or `quit` to end the session.

**Example:**
```
You : What's the weather like?
Assistant: I don't have eyes. Look outside.
You : exit
```

## Configuration

You can adjust the assistant's behavior by editing the constants at the top of `main.py`:

| Variable | Description |
|---|---|
| `MODEL` | The OpenAI model used for chat completions |
| `TEMPERATURE` | Controls response randomness (0 = deterministic, 2 = very random) |
| `SYSTEM_PROMPT` | Defines the assistant's personality/behavior |

## Project Structure

```
Simple-OpenAI-chatbot/
├── main.py          # Chatbot logic and CLI loop
├── requirements.txt # Python dependencies
├── .env.example      # Example environment file
└── README.md         # Project documentation
```

## Known Limitations

- No error handling for API/network failures
- No conversation length limit (long chats can grow the context indefinitely)
- No streaming responses — replies are printed only after full generation

## License

This project is open source and available under the [MIT License](LICENSE).
