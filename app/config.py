import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    POLYGON_API_KEY = os.getenv('POLYGON_API_KEY')
    DEBUG = True