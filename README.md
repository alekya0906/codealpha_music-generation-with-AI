# 🎵 AI Music Generator

## Overview

AI Music Generator is a Python-based application that generates music according to the user's selected mood. The application provides an interactive web interface built with Streamlit and creates MIDI music files using the Music21 library.

## Features

* Mood-based music generation
* Interactive Streamlit web interface
* Multiple mood options:

  * Happy
  * Sad
  * Calm
  * Energetic
* Automatic MIDI file generation
* Download generated music file
* Simple and user-friendly design

## Technologies Used

* Python
* Streamlit
* Music21
* NumPy

## Project Workflow

1. User selects a mood.
2. The system generates notes based on the selected mood.
3. A melody is created using Music21.
4. The generated music is saved as a MIDI file.
5. Users can download the generated music.

## Installation

Install the required libraries:

```bash
pip install streamlit
pip install music21
pip install numpy
```

## Run the Project

```bash
streamlit run music_generator.py
```

## Output

* Generates a MIDI music file (`generated_music.mid`)
* Allows users to download the generated music file

## Future Enhancements

* Real-time music playback
* Deep learning-based music generation
* Custom mood creation
* MP3/WAV audio export
* Advanced AI music composition models

## Author

Lakshmi Alekya
