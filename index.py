from perguntas import Pergunta, Pesquisa  

# Cria uma instância da classe Pesquisa utilizando como argumento a lista de perguntas. 
def main():

    # Definindo a lista de perguntas e utilizando a Classe Pergunta().
    # Criando instâncias da classe Pergunta com número e texto
    perguntas = [
        Pergunta(1, "Você sabe o que é um seguro de vida?"), 
        Pergunta(2, "Você possui atualmente um seguro de vida?"),
        Pergunta(3, "Você acredita que um seguro de vida é importante para proteger sua família financeiramente em caso de sua morte?"),
        Pergunta(4, "Você confia na seguradora para cumprir suas obrigações em caso necessário?"),
        Pergunta(5, "Você já teve alguma experiência pessoal ou familiar em que um seguro de vida foi acionado?"),
        Pergunta(6, "Você considera o custo do seguro de vida um fator importante ao decidir se deve ou não adquiri-lo?")
    ]
    pesquisa = Pesquisa(perguntas)
    pesquisa.verificaCodigo('Digite o código de identificação da pesquisa: ')  # Solicita e verifica o código fornecido.

    # Realiza a pesquisa e salva as respostas
    pesquisa.realizarPesquisa('Digite a idade do usuário: ', 'Digite o gênero do usuário (F/f para feminino, M/m para masculino ou O/o para outros): ')
    pesquisa.salvarPesquisas()
    
    
if __name__ == "__main__":
    main()
