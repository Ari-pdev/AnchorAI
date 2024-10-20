import webview
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
genai.configure(api_key=API_KEY)

generation_config = {
    "temperature": 2,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

chat_session = model.start_chat(
    history=[]
)


class JS_Python_Bridge_API():
    def log(self, value):
        print(value)

    def get_bot_response(self, user_input: str):
        print(chat_session.history)
        return chat_session.send_message(user_input).text


def start_webview():
    webview.create_window('Test', url="index.html",
                          js_api=JS_Python_Bridge_API())
    webview.start()


start_webview()
