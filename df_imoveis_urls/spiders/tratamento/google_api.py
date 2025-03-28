import pandas as pd
import numpy as np
import os
import re
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GOOGLE_API_KEY')

def get_address(latitude, longitude):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 'OK':
        return data['results'][0]['formatted_address']
    else:
        return "Endereço não encontrado"
    
# df["endereço"] = get_address(df["latitude"],df["longitude"])

print(get_address("-15.841232", "-48.020674"))