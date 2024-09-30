import random

def obter_mensagens_aleatoria():
    mensagens = [
        "Olá, mundo!",
        "Python é uma linguagem de programação poderosa.",
        "Vamos aprender a programar em Python!",
        "Mantenha o código limpo!",
        "Deixe as coisas simples"
    ]
    return random.choice(mensagens)