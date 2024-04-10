import csv
from datetime import datetime

class Pesquisa:
    def __init__(self, codigo):
        self.codigo = codigo
        # perguntas 
        self.perguntas = [
            "Nos últimos 3 meses você comprou chocolate nas Lojas Americanas?",
            "Nos últimos 3 meses você comprou bebida nas Lojas Americanas?",
            "Nos últimos 3 meses você comprou item de papelaria nas Lojas Americanas?",
            "Nos últimos 3 meses você comprou livro nas Lojas Americanas?"
        ]
        
        self.respostas = []

    def realizarPesquisa(self):
        # enquanto for verdade o codigo rodando 
        while True:

             # falta verificaçao de valores /tratamento de input
            idade = input("Digite a idade do usuário: ")
            if idade == '00':
                break
            genero = input("Digite o gênero do usuário: ")

            # criaçao de dict respostasUsuario com idade e genero.
            respostasUsuario = {'idade': idade, 'genero': genero}

            # perginta - loop for para pega perguntas, i - enumerate ira enumera a quantidade de perguntas na lista self.perguntas.
            for i, pergunta in enumerate(self.perguntas, start=1):
                resposta = input(f"{pergunta}\n1 - Sim\n2 - Não\n3 - Não sei responder\nResposta: ")
        
                # dependedo da quantidade de perguntas teremos a mesma quantidades de respostas.
                respostasUsuario[f'resposta_{i}'] = resposta 

            respostasUsuario['data_e_hora'] = datetime.now().strftime('%d/%m/%Y %H:%M') # data hora
            
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


