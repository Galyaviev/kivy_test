from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MainApp1(MDApp):
    def build(self):
        return MDLabel(text="Hello, World", halign="center")


MainApp1().run()