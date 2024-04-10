class Pergunta:
    def __init__(self, numero, texto):
        self.numero = numero
        self.texto = texto
    
    def pergunta(self):
        visual = int(input(f'''
            Pergunta {self.numero}:
                {self.texto}
                1 - Sim
                2 - Não
                3 - Não sei responder
                          '''))
        return visual