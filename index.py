from datetime import datetime
import csv
from perguntas import Pergunta, Pesquisa  # Importando classes relevantes do arquivo perguntas.py

# Definindo as perguntas como uma lista fora da classe pesquisa e utilizando a classe Pergunta() para formatação do visual e validação das respostas
perguntas = [
    Pergunta(1, "Você possui atualmente um seguro de vida?"),  # Criando instâncias da classe Pergunta com número e texto
    Pergunta(2, "Você sabe o que é um seguro de vida?"),
    Pergunta(3, "Você acredita que um seguro de vida é importante para proteger sua família financeiramente em caso de sua morte?"),
    Pergunta(4, "Você já considerou adquirir um seguro de vida para garantir o futuro de seus entes queridos?"),
    Pergunta(5, "Você sabe como funcionam os diferentes tipos de seguros de vida, como seguro de vida inteira e seguro de vida temporário?"),
    Pergunta(6, "Você sabe como funcionam os diferentes tipos de seguros de vida, como seguro de vida inteira e seguro de vida temporário?")
]

codigo_pesquisa = input('Digite o código de identificação da pesquisa: ')  # Solicita ao usuário o código de identificação da pesquisa

# Cria uma instância da classe Pesquisa com o código fornecido e a lista de perguntas
pesquisa = Pesquisa(codigo_pesquisa, perguntas)

# Realiza a pesquisa e salva as respostas
pesquisa.realizarPesquisa()
pesquisa.salvarPesquisas()
