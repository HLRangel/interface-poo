'''
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
'''
# main.py
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

# Importando todas as telas com as nomenclaturas do diagrama do grupo
from app.views.menu_screen import TelaInicial
from app.views.config_screen import TelaConfiguracao
from app.views.board_screen import TelaTabuleiro
from app.views.result_screen import TelaResultado
from app.controllers.game_controller import GameController

class BoardGameApp(MDApp):
    def build(self):
        # Tom de roxo aproximado dos botões do esboço
        self.theme_cls.primary_palette = 'DeepPurple'
        self.theme_cls.theme_style = 'Light'

        # Instancia o controlador (padrão de projeto obrigatório)
        self.controller = GameController()

        # Gerenciador de telas configurado com o fluxo completo do PlantUML
        sm = ScreenManager()
        sm.add_widget(TelaInicial(name='tela_inicial'))
        sm.add_widget(TelaConfiguracao(name='tela_configuracao', controller=self.controller))
        sm.add_widget(TelaTabuleiro(name='tela_tabuleiro', controller=self.controller))
        sm.add_widget(TelaResultado(name='tela_resultado', controller=self.controller))
        
        return sm

if __name__ == '__main__':
    BoardGameApp().run()