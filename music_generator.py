import streamlit as st
from music21 import stream, note
import random

st.title("🎵 AI Music Generator")
st.write(
    "This AI-powered application generates music based on the selected mood using Python and Music21."
)

mood = st.selectbox(
    "Select Mood",
    ["Happy", "Sad", "Calm", "Energetic"]
)

if st.button("Generate Music"):
    st.write(f"Selected Mood: {mood}")
    if mood == "Happy":
        notes_list = ['C4', 'E4', 'G4', 'C5']

    elif mood == "Sad":
        notes_list = ['A3', 'C4', 'E4', 'A4']

    elif mood == "Calm":
        notes_list = ['D4', 'F4', 'A4', 'D5']

    else:
        notes_list = ['C4', 'D4', 'E4', 'G4', 'A4', 'C5']

    melody = stream.Stream()

    for i in range(50):
        random_note = random.choice(notes_list)
        melody.append(note.Note(random_note))

    melody.write('midi', fp='generated_music.mid')

    st.success("Music Generated Successfully!")

with open("generated_music.mid", "rb") as file:
    st.download_button(
        label="Download Music",
        data=file,
        file_name="generated_music.mid",
        mime="audio/midi"
    )

    