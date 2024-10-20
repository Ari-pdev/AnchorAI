import webview


def start_webview():
    webview.create_window('Test', url="index.html")
    webview.start()


def main():
    start_webview()


main()
