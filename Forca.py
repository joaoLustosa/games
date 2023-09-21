#Jogo da Forca

import random
from os import system, name


def limpa_tela():

  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')

def start():
  limpa_tela()

  print("\nForca dos Bichos do Mar")
  print("Adivinhe a palavra abaixo:\n")

  palavras = ['baleia', 'peixe', 'caranguejo', 'raposa']
  palavra = random.choice(palavras)
  letras_descobertas = ['_' for letra in palavra]
  letras_erradas = []
  chances = 6

  while chances > 0:
    print(" ".join(letras_descobertas))
    print(f'\nChances restantes: {chances}')
    print(f'Letras erradas: {" ".join(letras_erradas)}')

    tentativa = input("\nDigite uma letra: ")
    tentativa = tentativa.lower()

    if tentativa in palavra:
      index = 0
      for letra in palavra:
        if tentativa == letra:
          letras_descobertas[index] = tentativa
        index += 1
    else:
      chances -= 1
      letras_erradas.append(tentativa)

    if '_' not in letras_descobertas:
      print(f'\nVocê venceu, a palavra era {palavra}!!')
      break

  if '_' in letras_descobertas:
    print(f'\nVocê perdeu, a palavra era {palavra}!!')

if __name__ == "__main__":
  start()