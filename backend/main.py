# Main import

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

# Custom function imports
from functions.openai_requests import convert_audio_to_text

# Initiate App
app = FastAPI()

# CORS - Origins
origins = ["https://localhost:5173",
           "https://localhost:5174",
           "https://localhost:4173",
           "https://localhost:4174",
           "https://localhost:3000"]

# CORS-Middleware
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

# Check health


@app.get("/health")
async def check_health():
    return {"message": "Healthy"}

# Post bot response
# Note: Not playing in browser when using post request

# Get audion


@app.get("/post-audio-get/")
async def get_audion():
    # Get saved audio
    audio_input = open("voice.mp3", "rb")

    # Decode audio
    messsage_decoded = convert_audio_to_text(audio_input)

    print(messsage_decoded)
    return "Done"
