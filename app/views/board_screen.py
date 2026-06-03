# app/views/board_screen.py
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout

class TelaTabuleiro(Screen):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller  # Guarda o controller recebido do main.py
        
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)
        layout.add_widget(MDLabel(text="Tela do Tabuleiro (3x)\nEm construção", halign="center", font_style="H4"))
        
        self.add_widget(layout)