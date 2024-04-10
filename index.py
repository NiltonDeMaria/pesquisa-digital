from perguntas import Pesquisa

# talvez acrescentar uma def main() para inicia o codigo 
# def main():
codigo_pesquisa = input('Digite o código de identificação da pesquisa: ')
pesquisa = Pesquisa(codigo_pesquisa)
pesquisa.realizarPesquisa()
pesquisa.salvarPesquisas()
        