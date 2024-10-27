
### Building the voice component
To implement voice functionality in the assistant, it is essential to have the right components for audio processing.

#### On macOS:
MacOS users can easily install the necessary libraries using Homebrew. Simply execute the following commands in the terminal:

brew install portaudio
brew install ffmpeg
These commands install PortAudio, which is essential for handling real-time audio, and FFmpeg, which provides tools for manipulating and converting audio formats.

#### On Windows (WSL):
For Windows users using WSL, the process is a little different. First, usbipd must be installed by running the following command in the Windows terminal:

winget install usbipd
Next, you need to open a WSL terminal and run:

sudo apt install ffmpeg
These steps ensure that the audio environment is correctly configured, allowing voice input capture and audio playback in the wizard.