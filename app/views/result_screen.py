# app/views/result_screen.py
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout

class TelaResultado(Screen):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)
        layout.add_widget(MDLabel(text="Tela de Resultados\nEm construção", halign="center", font_style="H4"))
        
        self.add_widget(layout)