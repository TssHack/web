from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.webview import WebView

class MyWebViewApp(App):
    def build(self):
        layout = BoxLayout()
        webview = WebView(url="https://yourwebsite.com")  # آدرس سایت شما
        layout.add_widget(webview)
        return layout

if __name__ == "__main__":
    MyWebViewApp().run()
