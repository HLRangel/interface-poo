# app/views/menu_screen.py
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.anchorlayout import MDAnchorLayout

class TelaInicial(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # 1. Layout base que serve puramente para centralizar tudo na tela
        layout_central = MDAnchorLayout(
            anchor_x='center',
            anchor_y='center'
        )
        
        # 2. Caixa vertical que vai segurar os elementos organizados
        # O 'adaptive_height=True' faz a caixa ter exatamente a altura dos elementos dentro dela
        caixa_conteudo = MDBoxLayout(
            orientation='vertical', 
            spacing=30,
            adaptive_height=True
        )
        
        # Título "3x" do esboço (Página 3) com o 'x' em vermelho
        titulo = MDLabel(
            text="3[color=ff0000]x[/color]", 
            markup=True,
            halign="center", 
            font_style="H1",
            bold=True,
            size_hint_y=None,
            height="100dp"
        )
        
        # Botão centralizado para iniciar
        btn_iniciar = MDRaisedButton(
            text="Iniciar Jogo",
            pos_hint={"center_x": 0.5},
            padding=[20, 10]
        )
        btn_iniciar.bind(on_release=self.ir_para_configuracao)
        
        # Monta a estrutura de herança visual dos elementos
        caixa_conteudo.add_widget(titulo)
        caixa_conteudo.add_widget(btn_iniciar)
        
        layout_central.add_widget(caixa_conteudo)
        self.add_widget(layout_central)

    def ir_para_configuracao(self, instance):
        # Transição de tela mapeada no PlantUML do grupo
        self.manager.current = 'tela_configuracao'