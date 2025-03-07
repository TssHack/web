from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.webview import WebView

# تابعی برای خواندن لینک از فایل
def get_website_url():
    try:
        with open("config.txt", "r") as file:
            url = file.readline().strip()
            return url if url else "https://default-url.com"  # در صورت خالی بودن، آدرس پیش‌فرض قرار می‌دهد
    except FileNotFoundError:
        return "https://default-url.com"  # اگر فایل نبود، یک مقدار پیش‌فرض برمی‌گرداند

class MyWebViewApp(App):
    def build(self):
        layout = BoxLayout()
        webview = WebView(url=get_website_url())  # دریافت لینک از فایل
        layout.add_widget(webview)
        return layout

if __name__ == "__main__":
    MyWebViewApp().run()
