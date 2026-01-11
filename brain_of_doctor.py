# Step 1: Setup GROQ API Key
import os
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# Step 2: Convert image to required format
import base64

image_path="acne.jpg"
image_file = open(image_path, "rb")
encoded_image=base64.b64encode(image_file.read()).decode("utf-8")
# Step 3: Setup multimodal LLM 
from groq import Groq



client = Groq(api_key=GROQ_API_KEY)
query="What skin condition is shown in this image?"
model="meta-llama/llama-4-maverick-17b-128e-instruct"
messages=[{
    "role": "user",
    "content":[
        { "type":"text",
         "text": query
        },
        {"type":"image_url",
         "image_url":{
             "url":f"data:image/jpeg;base64,{encoded_image}"
         },
    },
    
    ], 
 
}]
chat_completion=client.chat.completions.create(
    messages=messages,
    model=  model
)

print(chat_completion.choices[0].message.content)