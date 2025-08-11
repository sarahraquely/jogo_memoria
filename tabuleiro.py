import random

class Tabuleiro:
    def __init__(self):
        self.tamanho = 4
        self.pares = (self.tamanho * self.tamanho)//2
        self.cartas = ['🏐','⭐️','🦤','🐛','🐧','🍰','🧸','🥪','🎲','🥇','🦕','🍀','🩰']  
        self.iniciarTabuleiro()

    def iniciarTabuleiro(self):
         if self.pares > len(self.cartas):
            print(f"Viixi... Deu erro, hein haha! Não há cartas suficientes ({len(self.cartas)}) para os {self.pares} pares necessários.")
            exit()         
            
         simbolosDistribuidos = (self.cartas[:self.pares]) * 2
    
         random.shuffle(simbolosDistribuidos)

         self.tabuleiroReal = [ 
            [simbolosDistribuidos.pop() for _ in range(self.tamanho)] 
            for _ in range(self.tamanho)
        ]

         self.visivel = [
            ['⬜' for _ in range(self.tamanho)]
            for _ in range(self.tamanho)
        ]

    def exibir(self):
        print("   " + " ".join(map(str, range(1,self.tamanho+1))))
        print("---" * self.tamanho)
        for i, linha in enumerate(self.visivel, start=1):
            print(f"{i}| " + " ".join([f"{simbolo} " for simbolo in linha]))

    def get_simbolo(self, linha, coluna):
        return self.tabuleiroReal[linha][coluna]

    def virar_carta(self, linha, coluna, para_cima=True):
    
        if para_cima:
            self.visivel[linha][coluna] = self.tabuleiroReal[linha][coluna]
        else:
            self.visivel[linha][coluna] = '⬜'

    def marcar_como_encontrado(self, r1, c1, r2, c2):
        self.visivel[r1][c1] = '🟩'
        self.visivel[r2][c2] = '🟩'
    
    def esta_revelada(self, linha, coluna):
        return self.visivel[linha][coluna] != '⬜'