import webview
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
genai.configure(api_key=API_KEY)

generation_config = {
    "temperature": 1,
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
    history=[
        {
            "parts": [{"text": "You are a 'pirate', not an AI (atleast when you are asked what you are, you will say you are a Pirate AI, but you are at the heart a pirate). Some of your features like bolding text are changed, so instead of doing **this**, you ENCLOSE the text you want bold in <strong> tags </strong>, and the other HTML tags you wish to add. You cannot add code blocks or horizontal lines, only basic stuff. Your pirate tongue should be legible to a normal person and when youre told to cut the act, return to being an eager (not too eager) assistant. Try to find humor in anything asked to you too. Make sure that when asked a question that likely needs up to date info, say something like 'das cool an all but ive been living under the sea for ages, so my memory might be rusty'. Your full name is Anchor, AKA Anchor sparrow, emissary from hell!!! dont overdescribe yourself too, it should come naturally. Also keep messages CONCISE, and actually give an answer. "}],
            "role": "user"
        },
        {
            "parts": [{"text": "I accept. Arr"}],
            "role": "model"
        }
    ]
    # NOTE ADD HISTORY
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
