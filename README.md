# **Sonya: your voice assistant**
This project is a voice assistant built with open-source technologies, using *SpeechRecognition* to convert spoken language into text and *LangGraph* as the orchestration framework to create a multi-agent system that enables Sonya to handle multiple tasks.

The process begins with the user’s voice capture, which is converted into text for processing. This text serves as input to a decision node, which evaluates the user’s request and determines which tasks to execute from the four available options:

1. Schedule a meeting in the calendar.
1. Compose an e-mail with a specific message.
1. Respond to a question via an internet search.
1. Plan a trip including finding flights, hotels and suggestions for the right clothes to pack for the time of year.  

> [!NOTE]  
>  A multi-agent system requires calling to an LLM, so you will need an API KEY to run the proyect. In our case we chose to use **gpt-4o-mini**.

## **Usage**
A frontend has been created to test the program. To get started, clone the repository and run the following commands from the root folder:
```
poetry shell
poetry install
poetry run python scripts/run_assistant.py
```
After running these commands, click the localhost link provided in the terminal, and the frontend developed in Streamlit will appear, allowing Sonya to assist you with your tasks!

> [!TIP]
> If you want to switch languges, change it in the src/assistant/config.py file
> changing this variable for one of the available languages. **By default is in spanish.**
> ```
> LANGUAGE = "spanish"
> LANGUAGE = "english"
>```

## **Building the voice component**
To implement voice functionality in the assistant, it is essential to have the right components for audio processing.

### On macOS:
MacOS users can easily install the necessary libraries using Homebrew. Simply execute the following commands in the terminal:

```
brew install portaudio
brew install ffmpeg
```

These commands install PortAudio, which is essential for handling real-time audio, and FFmpeg, which provides tools for manipulating and converting audio formats.

### On Windows (WSL):
For Windows users using WSL, the process is a little different. First, usbipd must be installed by running the following command in the Windows terminal:
```
winget install usbipd
```
Next, you need to open a WSL terminal and run:
```
sudo apt install ffmpeg
```
These steps ensure that the audio environment is correctly configured, allowing voice input capture and audio playback in the wizard.

## **Contributors**
- [dmoya@syntonize.com](https://github.com/dimc26)  
  - [Linkedin profile](https://www.linkedin.com/in/diego-moya-c%C3%B3rdoba-98b155195/?original_referer=https%3A%2F%2Fwww%2Egoogle%2Ecom%2F&originalSubdomain=es)
- [agarciag@syntonize.com](https://github.com/Anuko50)  
  - [Linkedin profile](https://www.linkedin.com/in/ana-garc%C3%ADa-galindo/?originalSubdomain=es)
