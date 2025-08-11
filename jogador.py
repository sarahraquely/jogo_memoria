class Jogador:

    def __init__(self):
        self.nome = ""  
        self.pares_encontrados = 0
        self.escolherNome() 

    def escolherNome(self):

        while True: 
            nome_digitado = input("Escolha seu nome de jogador: ").strip() 
            if nome_digitado: 
                self.nome = nome_digitado
                print(f"Olá, {self.nome}! Bem-vindo(a) ao Jogo da Memória.")
                break 
            else:
                print("O nome não pode ser vazio. Por favor, tente novamente.")

    def get_nome(self):
        return self.nome
    
    def incrementar_pares(self):
        self.pares_encontrados += 1

    def get_pares_encontrados(self):
        return self.pares_encontrados