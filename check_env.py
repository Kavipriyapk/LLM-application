from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

print("KEY =", os.getenv("GOOGLE_API_KEY"))