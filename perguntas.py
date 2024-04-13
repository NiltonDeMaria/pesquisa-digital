#Versão atual com versões de todos os membros

import csv
from datetime import datetime

#Classe que constrói o visual das perguntas e trata erros de resposta como outros valores númericos ou letras
class Pergunta:
    def __init__(self, numero, texto):
        self.numero = numero
        self.texto = texto
    
    def pergunta(self):
        while True: 
            try:
                resposta = int(input(f''' 

Pergunta {self.numero}:
{self.texto}
1 - Sim
2 - Não
3 - Não sei responder
=>  '''))
                if resposta in [1,2,3]:
                    return resposta
                else:
                    print("Resposta inválida! Digite o número que corresponde a sua reposta!")     
            except ValueError:
                    print("Resposta inválida! Digite o número que corresponde a sua reposta!")


# Criando a classe pesquisa e passando como parâmentro o codigo da pesquisa e as perguntas (que serão criadas como uma lista fora da classe)
class Pesquisa:
    def __init__(self, codigo, pergutas):
        self.codigo = codigo
        self.perguntas = pergutas
        self.respostas = []


    def realizarPesquisa(self):
        while True:
            #Iniciando idade e genêro e declarando o valor indefinido/vazio, no mesmo escopo de "resposta usuario"
            idade = None
            genero = None
            
            #Verifica idade, sendo apenas permitido respostas para pessoas com +18 anos
            #Trata erros de entrada e finaliza o programa caso seja informado a idade 00
            while True:
                try:
                    idade = int(input("Digite a idade do usuário: "))
                    if idade >= 18:
                        break
                    elif idade == 00:
                        return 00 
                    else:
                        print("A idade mínima para responder a pesquisa é 18 anos!")
                except ValueError:
                    print('Digite uma resposta válida!')
                if idade == 00: #Pegando o valor 00 retornado e parando o loop principal 
                    break
                
                #Trata erros na entrada de gênero, sendo apenas permitido F/f ou M/m  
            while True:
                genero = input("Digite o gênero do usuário (F/f para feminino, M/m para masculino): ").strip().upper() 
                if genero in ['F', 'M' ]:
                    genero = 'Feminino' if genero == 'F' else 'Masculino'
                    break    
                else:
                    print("Resposta inválida. Por favor, insira apenas F/f para feminino ou M/m para masculino.")
            

             # criaçao de dict respostasUsuario com idade e genero.    
            respostasUsuario = {'idade': idade, 'genero': genero}

            
            for perg in self.perguntas: # para cada pergunta na lista de perguntas da classe pesquisa
                    resposta = perg.pergunta() #Exibindo a pergunta, solicitando resposta e validando, valor retornado = a resposta (pergunta() da classe pergunta)
                    respostasUsuario[f'resposta_{perg.numero}'] = resposta  #Armazenando a resposta do usuario dentro de "resposta usuario" c o número da pergunta(classse pergunta)
           
            respostasUsuario['data_e_hora'] = datetime.now().strftime('%d/%m/%Y %H:%M')# data hora
            
            #  acrescentado respostasUsuario na lista self.respostas dentro de atributos Pesquisa fora do loop
            self.respostas.append(respostasUsuario)
           

    def salvarPesquisas(self):
        with open(f'respostas{self.codigo}.csv', 'w', newline='', encoding='utf-8') as csvfile:

            # criando cabeçalho com os valores chaves do primeiro elemento da lista self.respostas
            campos_head = [x for x in self.respostas[0]]

            writer = csv.DictWriter(csvfile, fieldnames=campos_head)
            writer.writeheader()
            for resposta in self.respostas:
                writer.writerow(resposta)

