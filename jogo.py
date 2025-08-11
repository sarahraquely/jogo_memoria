import time
import os

from tabuleiro import Tabuleiro
from jogador import Jogador

class Jogo:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.total_tentativas = 0
       
        print("Configurando Jogador 1:")
        self.jogador1 = Jogador()
        print("\nConfigurando Jogador 2:")
        self.jogador2 = Jogador()

        self.jogadores = [self.jogador1, self.jogador2]
        self.jogador_atual_indice = 0
    
    def _limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _get_jogador_atual(self):
        return self.jogadores[self.jogador_atual_indice]

    def _proximo_jogador(self):
        self.jogador_atual_indice = (self.jogador_atual_indice + 1) % len(self.jogadores)

    def _todos_pares_encontrados(self):
     pares_totais_encontrados = sum(jogador.get_pares_encontrados() for jogador in self.jogadores)
     return pares_totais_encontrados == self.tabuleiro.pares

    def _obter_coordenadas_validas(self, mensagem):
        while True:
            try:
              
                coord_str = input(f"{self._get_jogador_atual().get_nome()}, {mensagem} (linha coluna, ex: 0 1): ") 
                r, c = map(int, coord_str.split())
                
                if not (0 <= r < self.tabuleiro.tamanho and 0 <= c < self.tabuleiro.tamanho):
                    print("Coordenadas inválidas, né... Tente novamente.")
                elif self.tabuleiro.esta_revelada(r, c): 
                    print("Essa carta já tá até virada já. Escolha outra.")
                else:
                    return r, c
            except ValueError:
                print("Af, não é desse jeito. Digite dois números separados por espaço.")

    def iniciar_jogo(self):
        time.sleep(1) 
        self._loop_principal()

    def _loop_principal(self):
        while not self._todos_pares_encontrados(): 
            self._limpar_tela()
            self.tabuleiro.exibir()
            
            print(f"\n--- PLACAR ---")
            print(f"{self.jogador1.get_nome()}: {self.jogador1.get_pares_encontrados()} pares")
            print(f"{self.jogador2.get_nome()}: {self.jogador2.get_pares_encontrados()} pares")
            print(f"----------------")
            print(f"\nÉ a vez de: {self._get_jogador_atual().get_nome()} | Tentativas totais: {self.total_tentativas}")
            
            
            print("\nEscolha a primeira carta:")
            r1, c1 = self._obter_coordenadas_validas("Escolha a primeira carta")
            self.tabuleiro.virar_carta(r1, c1, para_cima=True)
            
            self._limpar_tela()
            self.tabuleiro.exibir()

            print("\nEscolha a segunda carta:")
            r2, c2 = self._obter_coordenadas_validas("Escolha a segunda carta")
            
            if (r1, c1) == (r2, c2):
                print("Ué! Você escolheu a mesma carta, né... Perdeu a vez agora.")
                time.sleep(1.5)
                self.tabuleiro.virar_carta(r1, c1, para_cima=False)
                self._proximo_jogador()
                continue
                        
            self.tabuleiro.virar_carta(r2, c2, para_cima=True)
            self._limpar_tela()
            self.tabuleiro.exibir()

            self.total_tentativas += 1

            if self.tabuleiro.get_simbolo(r1, c1) == self.tabuleiro.get_simbolo(r2, c2):
                print("PEGA! Arrasou muito!")
                self.tabuleiro.marcar_como_encontrado(r1, c1, r2, c2)
                self._get_jogador_atual().incrementar_pares()
                time.sleep(1.5)
            else:
                print("Errou errou")
                time.sleep(2) 
                self.tabuleiro.virar_carta(r1, c1, para_cima=False)
                self.tabuleiro.virar_carta(r2, c2, para_cima=False)
                self._proximo_jogador()
        
        self._finalizar_jogo()

    def _finalizar_jogo(self):
        self._limpar_tela()
        self.tabuleiro.exibir()

        print(f"\n--- FIM DE JOGOOO ---")

        print(f"{self.jogador1.get_nome()}: {self.jogador1.get_pares_encontrados()} pares")
        print(f"{self.jogador2.get_nome()}: {self.jogador2.get_pares_encontrados()} pares")

        if self.jogador1.get_pares_encontrados() > self.jogador2.get_pares_encontrados():
            print(f"\n🏆 AEEE, {self.jogador1.get_nome()}! você ganhou. 🏆")
        elif self.jogador2.get_pares_encontrados() > self.jogador1.get_pares_encontrados():
            print(f"\n🏆 Parabéns, {self.jogador2.get_nome()}! Você é o VENCEDOR! 🏆")
        else:
            print(f"\n🤝 EMPATOU! Os dois jogadores encontraram {self.jogador1.get_pares_encontrados()} pares. 🤝")
        
        print(f"Total de tentativas no jogo: {self.total_tentativas}")
        print("Obrigado por jogar!")