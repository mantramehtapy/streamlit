import streamlit as st
from os import write

st.header("Mantra's website")

#image
from PIL import Image
img = Image.open("/home/linuxdom/Desktop/streamlit/ZtyeaB.jpg")
st.image(img,width=500)

#video
vid_files = open("/home/linuxdom/Desktop/streamlit/20210129_144034.mp4","rb").read()
st.video(vid_files)

#audio
audio_files = open("/home/linuxdom/Desktop/streamlit/gamer.mp3","rb").read()
st.audio(audio_files,format="audio/mp3")

#bollon
if st.button("ballons"):
    st.balloons()

st.text("website made by Mantra.Mehta for any questions here is my gmail")

st.text("mantra.mehta@gmail.com")

st.write("check out my [discord](https://discord.gg/ZHqCEqb7)")

st.write("check out my [github](https://github.com/mantramehtapy)")