# app/views/config_screen.py
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel

class TelaConfiguracao(Screen):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.add_widget(MDLabel(text="Tela de Configuração (Em construção)", halign="center"))