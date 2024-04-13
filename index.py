from perguntas import *

#Definindo as perguntas como uma lista fora da classe pesquisa e utilizando a classe Pergunta() para formatação do visual e validção das respostas
perguntas =  [
            Pergunta(1, "Você possui atualmente um seguro de vida?"),
            Pergunta(2, "Você sabe o que é um seguro de vida?"),
            Pergunta(3, "Você acredita que um seguro de vida é importante para proteger sua família financeiramente em caso de sua morte?"),
            Pergunta(4, "Você já considerou adquirir um seguro de vida para garantir o futuro de seus entes queridos?"),
            Pergunta(5, "Você sabe como funcionam os diferentes tipos de seguros de vida, como seguro de vida inteira e seguro de vida temporário?"),
            Pergunta(6, "Você sabe como funcionam os diferentes tipos de seguros de vida, como seguro de vida inteira e seguro de vida temporário?")
        ]


codigo_pesquisa = input('Digite o código de identificação da pesquisa: ')
pesquisa = Pesquisa(codigo_pesquisa , perguntas) #Iniciando a pesquisa com os parametros de codigo e das perguntas da lista
pesquisa.realizarPesquisa()
pesquisa.salvarPesquisas()
