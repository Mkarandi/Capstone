import os
import openai
import requests
from dotenv import load_dotenv

openai.api_key = os.getenv("OPENAI_API_KEY")

nft_image = openai.Image.create(
  prompt="Dracula in a fishing boat catching a big fish",
  n=2,
  size="1024x1024"
)

nft_image
nft_image_link = nft_image["data"][0]["url"]

print(nft_image_link)
