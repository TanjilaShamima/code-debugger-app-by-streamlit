from google import genai
from dotenv import load_dotenv

import os

# load environment variables from .env file
load_dotenv()

gen_api_key = os.getenv("GEMINI_API_KEY")

# initialize the Gemini API client
client = genai.Client(api_key = gen_api_key)

# function to perform AI operations based on user input
def perform_ai_operations(pil_images, options):
    # Simulate AI processing based on selected options
    prompt = f"Perform the operation '{options}' on the following images and provide the results."
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[pil_images, prompt]
    )
    return response.text