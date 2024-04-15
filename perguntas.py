# Importa o módulo datetime para manipulação de data e hora
from datetime import datetime  

# Importa o módulo csv para trabalhar com arquivos CSV
import csv  

# Definição da classe Pergunta
class Pergunta:
    def __init__(self, numero, texto):
        self.numero = numero  # Atributo para armazenar o número da pergunta
        self.texto = texto    # Atributo para armazenar o texto da pergunta
    
    # Método para apresentar a pergunta ao usuário e obter a resposta
    def pergunta(self):
        while True: 
            try:
                # Apresenta a pergunta ao usuário e solicita a resposta
                resposta = int(input(f''' 

Pergunta {self.numero}:
{self.texto}
1 - Sim
2 - Não
3 - Não sei responder
=>  '''))
                # Verifica se a resposta está dentro das opções válidas (1, 2 ou 3)
                if resposta in [1, 2, 3]:
                    return resposta
                else:
                    print("Resposta inválida! Digite o número que corresponde à sua resposta!")     
            except ValueError:
                # Trata a exceção se o usuário não inserir um número válido
                print("Resposta inválida! Digite o número que corresponde à sua resposta!")

# Definição da classe Pesquisa
class Pesquisa:
    def __init__(self, codigo, perguntas):
        self.codigo = codigo        # Atributo para armazenar o código da pesquisa
        self.perguntas = perguntas  # Atributo para armazenar a lista de perguntas
        self.respostas = []         # Atributo para armazenar as respostas dos usuários

    # Método para realizar a pesquisa
    def realizarPesquisa(self):
        while True:
            idade = None
            genero = None

            try:
                # Solicita a idade do usuário
                idade = int(input("Digite a idade do usuário (ou digite 00 para sair): "))

                # Verifica se o usuário digitou 0 para sair da pesquisa
                if idade == 0:
                    print("Saindo da pesquisa...")
                    return
                
                # Verifica se a idade é menor que 18 anos
                elif idade < 18:
                    print("A idade mínima para responder a pesquisa é 18 anos!")
                    continue
            except ValueError:
                
                # Trata exceção se o usuário digitar algo que não é um número
                print('Digite uma resposta válida!')
                continue

            while True:
                # Solicita o gênero do usuário
                genero = input("Digite o gênero do usuário (F/f para feminino, M/m para masculino): ").strip().upper()
                # Verifica se o gênero é válido (F ou M)
                if genero in ['F', 'M']:
                    genero = 'Feminino' if genero == 'F' else 'Masculino'
                    break
                else:
                    print("Resposta inválida. Por favor, insira apenas F/f para feminino ou M/m para masculino.")

            # Cria um dicionário com as respostas do usuário
            respostasUsuario = {'idade': idade, 'genero': genero}

            # Pergunta todas as perguntas e armazena as respostas no dicionário
            for perg in self.perguntas:
                resposta = perg.pergunta()
                respostasUsuario[f'resposta_{perg.numero}'] = resposta

            # Adiciona a data e hora atual ao dicionário de respostas
            respostasUsuario['data_e_hora'] = datetime.now().strftime('%d/%m/%Y %H:%M')
            
            # Adiciona o dicionário de respostas à lista de respostas da pesquisa
            self.respostas.append(respostasUsuario)

    # Método para salvar as respostas em um arquivo CSV
    def salvarPesquisas(self):
        with open(f'respostas{self.codigo}.csv', 'w', newline='', encoding='utf-8') as csvfile:

            # Verifica se há respostas para salvar
            if self.respostas:

                # Obtém os nomes das colunas (cabeçalho) a partir das chaves do primeiro dicionário de respostas
                campos_head = list(self.respostas[0].keys())

                # Cria um escritor de CSV com os campos (colunas) definidos
                writer = csv.DictWriter(csvfile, fieldnames=campos_head)

                # Escreve o cabeçalho no arquivo CSV
                writer.writeheader()

                # Escreve cada linha (resposta) no arquivo CSV
                for resposta in self.respostas:
                    writer.writerow(resposta)
            else:
                # Caso não haja respostas, imprime uma mensagem informando ao usuário
                print("Não há respostas para salvar.")
