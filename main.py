from kivymd.app import MDApp
from kivy.lang import Builder

class BoardGameApp(MDApp):
    def build(self):
        return Builder.load_file("app/views/title.kv")

if __name__ == '__main__':
    BoardGameApp().run()