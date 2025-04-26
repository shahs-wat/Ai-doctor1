import os
import base64
from groq import Groq

# Setup GROQ API key
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# Function to encode image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Analyze image with query
def analyze_image_with_query(query, model, encoded_image):
    client = Groq()  
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}},
            ]
        }
    ]
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content
