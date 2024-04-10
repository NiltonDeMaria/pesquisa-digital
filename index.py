import csv
from datetime import datetime

def pergunta(numero, texto):
    visual = int(input(f'''
        Pergunta {numero}:
            {texto}
            1 - Sim
            2 - Não
            3 - Não sei responder
                          '''))
    return visual

codigo = input('Digite o código de identificação da pesquisa: ')

with open(f'respostas{codigo}.csv', 'w', newline='') as csvfile:
            campos_head = ['idade', 'genero', 'resposta_1', 'resposta_2', 'resposta_3', 'resposta_4', 'data e hora']
            writer = csv.DictWriter(csvfile, fieldnames=campos_head)

            writer.writeheader()
            
            idade = 3

            while idade != 00:
                     
                idade = int(input("Digite a idade do usuário: "))
                
                if idade == 00:
                    break

                genero = input("Digite o gênero do usuário: ")

                resposta1 = pergunta(1, "Nos últimos 3 meses você comprou chocolate nas Lojas Americanas?")
                
                resposta2 = pergunta(2, "Nos últimos 3 meses você comprou bebida nas Lojas Americanas?")
                
                resposta3 = pergunta(3, "os últimos 3 meses você comprou item de papelaria nas Lojas Americanas?")
                
                resposta4 = pergunta(4 , "Nos últimos 3 meses você comprou livro nas Lojas Americanas?")
                
                data_hora = datetime.now().strftime('%d/%m/%Y %H:%M')
                

                writer.writerow({'idade': idade, 'genero': genero, 'resposta_1':resposta1, 'resposta_2':resposta2, 'resposta_3': resposta3, 'resposta_4':resposta4, 'data e hora': data_hora})

        