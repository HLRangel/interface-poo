# 2º Projeto POO

## Estrutura dos diretórios

- `special/` - Contém dados de documentação/dados relacionados ao projeto, como diagramas UML e PDFs.

## Esboços e Diagrama UML

## Esboços

Os esboços em PDF se encontram [em special/esbocos.pdf](special/esbocos.pdf).

## Diagrama UML do projeto

![Um diagrama UML do projeto](special/diagrama.png)

[PDF](special/esbocos.pdf)
[Arquivo PlantUML](special/diagrama.pu)

## Instruções de instalação

Se necessário, crie um ambiente virtual:

`python3 -m venv poo_env`

Ative o ambiente virtual:

`source ./poo_env/bin/activate`

Depois, instale os pré-requisitos:

`pip install -r requirements.txt`

## Instruções de utilização

Com o ambiente virtual ativo, execute o comando:

`python main.py`

# Uso de LLMs

**Obs:** Este projeto faz uso de um arquivo `AGENTS.md` para forçar que a geração de código e documentação por modelos de linguagem se dê de uma forma minimamente concisa.

- ChatGPT (GPT-5.5-Instant): *Troubleshooting* da sintáxe PlantUML (PlantText), que foi a ferramenta de renderização utilizada para criação do diagrama vinculado ao projeto. Implementação inicial de `app/controllers/game_controller.py`.

- Claude (Claude Sonnet 4.6): *Troubleshooting* de problemas de renderização e sintaxe KV, auxilio na estruturação de classes.