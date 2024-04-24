# Ansar Khan

import base64
import requests
import io
from django.conf import settings

def encode_image(image_path):
  with io.open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def perform_analysis(image_path):
    image_path = image_path.lstrip('/')
    base64_image = encode_image(image_path)
    headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {settings.OPENAI_API_KEY}"
    }
    payload = {
      "model": "gpt-4-vision-preview",
      "messages" :[
        {
          "role": "user",
          "content": [
            {"type": "text", "text": "What’s in this image?"},
            {
              "type": "image_url",
              "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
              },
            },
          ],
        }
      ],
      "max_tokens": 300,
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    return {'description': response.json()}