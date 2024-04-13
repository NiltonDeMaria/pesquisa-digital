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


  # perguntas 
class Pesquisa:
    def __init__(self, codigo):
        self.codigo = codigo
        self.perguntas = [
            Pergunta(1, "Nos últimos 3 meses você comprou chocolate nas Lojas Americanas?"),
            Pergunta(2, "Nos últimos 3 meses você comprou bebida nas Lojas Americanas?"),
            Pergunta(3, "Nos últimos 3 meses você comprou item de papelaria nas Lojas Americanas?"),
            Pergunta(4, "Nos últimos 3 meses você comprou livro nas Lojas Americanas?")
        ]
        self.respostas = []



    def realizarPesquisa(self):
        while True:
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
                if idade == 00:
                    break
                
                #Trata erros na entrada de gênero, sendo apenas permitido F/f ou M/m  
            while True:
                genero = input("Digite o gênero do usuário (F/f para feminino, M/m para masculino): ").strip().upper()
                if genero in ['F', 'f', 'M', 'm' ]:
                    genero = 'Feminino' if genero == 'F' else 'Masculino'
                    break    
                else:
                    print("Resposta inválida. Por favor, insira apenas F/f para feminino ou M/m para masculino.")
            
             # criaçao de dict respostasUsuario com idade e genero.    
            respostasUsuario = {'idade': idade, 'genero': genero}

           
            for pergunta in self.perguntas: # para cada pergunta na lista de perguntas(classe pesquisa)
                    resposta = pergunta.pergunta() #Exibindo a pergunta, solicitando resposta e validando, valor retornado = a resposta
                    respostasUsuario[f'resposta_{pergunta.numero}'] = resposta  #Armazenando a resposta do usuario dentro de "resposta usuario" c o número da pergunta

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

