from datetime import datetime  
import csv  

# Classe Pergunta: Define o visual e opções de resposta para cada pergunta na pesquisa.
# Solicita uma resposta ao usuário e a converte para 'Sim', 'Não' ou 'Não sei responder'. Trata os possíveis erros de entrada
class Pergunta:
    def __init__(self, numero, texto):
        self.numero = numero          
        self.texto = texto         
        self.opcoes  = [1, 2, 3]    
    
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
                if resposta in self.opcoes:  
                   return 'Sim' if resposta == 1 else ('Não' if resposta == 2 else 'Não sei responder')
                else:
                    print("Resposta inválida! Digite o número que corresponde à sua resposta!")     
            except ValueError:
                print("Resposta inválida! Digite o número que corresponde à sua resposta!") 


# Classe Pesquisa: Realiza a pesquisa com base em uma lista de perguntas.
class Pesquisa:
    def __init__(self, perguntas):
        self.perguntas = perguntas                 
        self.respostas = []                       
    
  # Verifica e armazena o código da pesquisa, garantindo que seja preenchido.  
    def verificaCodigo(self, msg):               
        while True:
            self.codigo = input(msg)              
            if self.codigo.strip():
               break                 
            else:
                print("Digite o código de pesquisa! ")   


  # Como regra de negocio a pesquisa só poderá ser feita com pessoas acima de 18 anos Sendo digitado idade = 00 a pesquisa é interrompida.
  # Coleta e verifica a idade do usuário. Trata possiveis erros de entrada.
    def realizarPesquisa(self, idadePergun, generoPergun):        
        while True:
            idade = None
            genero = None
            try:
                idade = int(input(idadePergun))   
                if idade == 00:             
                    print("Saindo da pesquisa...")
                    return 
                elif idade < 18:            
                    print("A idade mínima para responder a pesquisa é 18 anos!")
                    continue
            except ValueError:
                print('Digite uma resposta válida!')        
                continue

  #Coleta e verifica a entrada de gênero.
            while True:
                opcoesGenero =  ['F', 'M', 'O' ]                      
                genero = input(generoPergun).strip().upper()
                if genero in opcoesGenero:
                    genero = 'Feminino' if genero == 'F' else 'Masculino' if genero == 'M' else 'Outros' 
                    break   
                else:
                    print("Resposta inválida. Por favor, insira apenas F/f para feminino, M/m para masculino ou O/o para outros")


  # Para cada pergunta na lista de perguntas o método pergunta(Classe Pergunta()) é acionado e armazena a resposta em "resposta"
  # Cria as colunas do arquivo csv. As respostas são adicionadas ao dicionário (respostaUsuario) juntamente com a data e hora.
            respostasUsuario = {'idade': idade, 'genero': genero}   
            for perg in self.perguntas:      
                resposta = perg.pergunta() 
                respostasUsuario[f'resposta_{perg.numero}'] = resposta

            respostasUsuario['data_e_hora'] = datetime.now().strftime('%d/%m/%Y %H:%M') 
            
            self.respostas.append(respostasUsuario) 


  # Verifica se há respostas para salvar, caso não haja, imprime uma mensagem informando ao usuário
  # Obtém os nomes das colunas a partir da chave do primeiro dicionário resposta.
  # Armazena as respostas do usuário no arquivo csv.
    def salvarPesquisas(self):          
        with open(f'respostas{self.codigo}.csv', 'w', newline='', encoding='utf-8') as csvfile:

            if self.respostas: 
                campos_head = list(self.respostas[0].keys())   
                writer = csv.DictWriter(csvfile, fieldnames=campos_head)    # Cria um escritor de CSV com os campos (colunas) definidos
                writer.writeheader()                                    # Escreve o cabeçalho no arquivo CSV

                for resposta in self.respostas:   
                    writer.writerow(resposta)
            else:
                print("Não há respostas para salvar.")    