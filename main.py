import webview


class JS_Python_Bridge_API():
    def log(self, value):
        print(value)

    def get_bot_response(self, user_input: str):
        return user_input


def start_webview():
    window = webview.create_window('Test', url="index.html",
                                   js_api=JS_Python_Bridge_API())
    webview.start(debug=True)


def main():
    start_webview()


main()
