from perguntas import *

codigo_pesquisa = input('Digite o código de identificação da pesquisa: ')
pesquisa = Pesquisa(codigo_pesquisa)
pesquisa.realizarPesquisa()
pesquisa.salvarPesquisas()