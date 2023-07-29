# Voice Assistant with Text Summarization

This is a voice assistant program that uses the Bard API to fetch detailed answers to your queries and then provides a summary of the answer using text summarization. The program can open websites, play music, and answer questions using voice commands.

## Features

- **Voice Recognition:** The program can recognize voice commands using the `speech_recognition` library.

- **Web Browsing:** You can ask the assistant to open websites such as YouTube, Google, GitHub, Wikipedia, Amazon, Canva, and Flipkart.

- **Music Player:** The assistant can play random songs from a specified directory.

- **Text Summarization:** The program uses the Natural Language Toolkit (NLTK) to summarize the detailed answers fetched from the Bard API.

- **Greeting:** The assistant greets the user based on the time of day (morning, afternoon, evening).

## Requirements

- Python 3.x
- Install the required packages by running: `pip install -r requirements.txt`

## Setup

1. Clone the repository to your local machine.
2. Install the required packages using `pip install -r requirements.txt`.
3. Obtain a BARD API key from the [BARD website](https://bardapi.com/) and set it as an environment variable with the name `_BARD_API_KEY`.
4. Adjust the paths for the music directory according to your local setup.

## Usage

1. Run the program: `python voice_assistant.py`.
2. The voice assistant will greet you based on the time of day.
3. Say "Alexa" to activate the voice assistant.
4. Ask questions or give commands such as:
   - "Open YouTube"
   - "Play some music"
   - "What is the capital of France?"
   - "Exit"

The program will fetch the answers from the Bard API and provide a summarized response using text summarization.

## Supported Operating Systems

The program is supported on Windows, macOS, and Linux.

## Note

- The program may require an active internet connection to fetch answers from the Bard API and perform voice recognition.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
