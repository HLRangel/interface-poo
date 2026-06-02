from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

import app.models.classes as game

# ATENÇÃO! Não acessar o modelo diretamente da tela!
# Usar o pattern Controller (ver doc)

class BoardGameApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.theme_style = 'Light'

        sm = ScreenManager()
        return sm

if __name__ == '__main__':
    BoardGameApp().run()