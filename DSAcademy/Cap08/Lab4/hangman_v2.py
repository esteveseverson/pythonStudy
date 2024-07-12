import random
import os
import re

header = "    >>>>>>>>>>Hangman<<<<<<<<<<"

board = [
'''
\t\t+---+
\t\t|   |
\t\t    |
\t\t    |
\t\t    |
\t\t    |
\t\t=========''', 
'''
\t\t+---+
\t\t|   |
\t\tO   |
\t\t    |
\t\t    |
\t\t    |
\t\t=========''', 
'''
\t\t+---+
\t\t|   |
\t\tO   |
\t\t|   |
\t\t    |
\t\t    |
\t\t=========''', 
'''
\t\t +---+
\t\t |   |
\t\t O   |
\t\t/|   |
\t\t     |
\t\t     |
\t\t=========''', 
'''
\t\t +---+
\t\t |   |
\t\t O   |
\t\t/|\  |
\t\t     |
\t\t     |
\t\t=========''', 
'''
\t\t +---+
\t\t |   |
\t\t O   |
\t\t/|\  |
\t\t/    |
\t\t     |
\t\t=========''', 
'''
\t\t +---+
\t\t |   |
\t\t O   |
\t\t/|\  |
\t\t/ \  |
\t\t     |
\t\t=========''']

class Hangman:
    def __init__(self, word_to_guess):
        self.attempts = 6
        self.word_to_guess = word_to_guess.upper()  # converte a palavra para maiúsculas para padronização
        self.initialize_guess_word()

    def initialize_guess_word(self):
        self.guess_word = ['_' if caractere.isalpha() else caractere for caractere in self.word_to_guess]

    def imprimir_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(header)
        print(board[6 - self.attempts])

    def validate_letter(self):
        while True:
            print(f'\nLetras já utilizadas: {", ".join(repeated_letters)}')
            chosen_letter = input("\nEscolha uma letra (caso seja uma palavra, apenas a primeira letra será considerada): ").strip().upper()[:1]

            if re.match(r'^[a-zA-Z]$', chosen_letter) and chosen_letter not in repeated_letters:
                repeated_letters.append(chosen_letter)
                break
            else:
                self.imprimir_tela()
                print(f"A palavra que você está tentando adivinhar é: {''.join(self.guess_word)}")
                if chosen_letter in repeated_letters:
                    print(f"A letra '{chosen_letter}' já foi usada, por favor digite outra.")
                else:
                    print(f"'{chosen_letter}' não é uma letra válida, por favor digite outra.")

        return chosen_letter

    def correct_letter(self, verify_letter):
        letter_guessed = False
        for i, letter in enumerate(self.word_to_guess):
            if verify_letter == letter:
                if self.guess_word[i] == '_':
                    self.guess_word[i] = verify_letter
                    letter_guessed = True
        return letter_guessed

    def missing_letters(self):
        return sum(1 for x in self.guess_word if x == '_')

    def game_end(self):
        return self.missing_letters() == 0 or self.attempts == 0

    def player_win(self):
        return self.game_end() and self.missing_letters() == 0

# Funções fora da classe

def champion_select():
    champions_txt = "champions.txt"
    dict_champs = {}

    with open(champions_txt, "r", encoding="utf-8") as file:
        for line in file:
            lineSize = line.strip().split()
            if len(lineSize) == 3:
                champ_name = lineSize[0]
                champ_class = lineSize[2]
                dict_champs[champ_name] = champ_class
            elif len(lineSize) == 4:
                champ_name = lineSize[0] + ' ' + lineSize[1]
                champ_class = lineSize[3]
                dict_champs[champ_name] = champ_class

    random_champ = random.choice(list(dict_champs.items()))
    define_champion = random_champ[0]
    tip = random_champ[1]
    return define_champion, tip

# Início do jogo
repeated_letters = []
word_to_guess, tip = champion_select()
game = Hangman(word_to_guess)

while game.attempts > 0:
    game.imprimir_tela()
    print(f"Você ainda tem {game.attempts} tentativas.")
    print(f"A palavra que você está tentando adivinhar é: {''.join(game.guess_word)}")
    print(f"A dica é que a classe desse personagem é {tip}")
    verify_letter = game.validate_letter()
    if not game.correct_letter(verify_letter):
        game.attempts -= 1

    if game.player_win():
        game.imprimir_tela()
        print(f"Parabéns! Você adivinhou que era a {word_to_guess}.")
        break

else:
    game.imprimir_tela()
    print("Que pena! Você não conseguiu adivinhar a palavra.")
    print(f"A palavra era: {word_to_guess}")