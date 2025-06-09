from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

headers_auth = {
    "Authorization": API_KEY,
    "Content-Type": "application/json"
}
headers_auth_user_session = {
    "Authorization": API_KEY,
    "Content-Type": "application/json"
}