import random
import os
import re

# Abre o arquivo e faz um dicionário com os dados
def championSelect():

    champions_txt = 'champions.txt'
    dict_champs = {}

    with open(champions_txt, 'r', encoding='utf-8') as file:
        for line in file:
            lineSize = line.strip().split()
            if len(lineSize) == 3:
                champ_name = lineSize[0]
                champ_class = lineSize[2]
                dict_champs[champ_name] = champ_class
            elif len(lineSize) == 4:
                champ_name = lineSize[0] + ' ' + lineSize[1]
                champ_class = lineSize[3]

    campeao_aleatorio = random.choice(list(dict_champs.items()))
    nome_aleatorio, classe_aleatoria = campeao_aleatorio
    return campeao_aleatorio

# faz o cabeçalho
def hangmanHeader():
    os.system('cls')
    print('JOGO DA FORCA')
    print('Tema: Campeões de League of Legends\n-----------------------------------')

#faz a validação das letras inseridas, primeiro se é válida, caso seja valida vê se é repetida
def validate_letter():
    while True:

        print(f'\nLetras já utilizadas: {repeated_letters}\n')

        chosen_letter = input('\nEscolha uma letra (caso seja uma palavra, será considerada apenas a primeira letra): ').strip().upper()[:1]

        check_letter = lambda letter: bool(re.match(r'^[a-zA-Z]+$', letter))
        already_use = lambda letter: letter in repeated_letters

        if check_letter(chosen_letter):
            if not already_use(chosen_letter):
                repeated_letters.append(chosen_letter)
                break
            else:
                hangmanHeader()
                print(f'A palavra que você tem que adivinhar é´: {word}')
                print(f"'{chosen_letter}' já foi utilizada, favor escolher outra")
                print(f'Você ainda tem {max_attempts} tentativas\n')
        else:
            hangmanHeader()
            print(f'A palavra que você tem que adivinhar é´: {word}')
            print(f"'{chosen_letter}' não é uma letra válida, favor escolher outra")
            print(f'Você ainda tem {max_attempts} tentativas\n')

    return chosen_letter

# verifica se uma letra está na lista de letras da palavra escolhida
def check_correct_letter():
    if verify_letter in selected_champion:
        ids = [i for i, x in enumerate(selected_champion) if x == verify_letter]
        for i in ids:
            word[i] = verify_letter
        return True
    else:
        return False

#faz a lista com base na palavra escolhida, criando uma lista com o numero de letras em formato de underline
def guess_word():
    right_letters = []
    for caractere in selected_champion:
        if caractere.isalpha():
            right_letters.append('_')
        else:
            right_letters.append(caractere)
    return right_letters

#contador de quantas letras faltam para completar a palavra
def missing_letters():
    cont = 0
    for x in word:
        if x == '_':
            cont += 1
    print(f'\t\tAinda faltam {cont} letras')
    return cont

#tela de vitoria
def winner_panel():
    print('Parabéns você ganhou\n')
    print(f'Sobraram {max_attempts} tentativas e o campeão que você adivinhou foi {selected_champion}\n')
    print('FIM DA EXECUÇÃO DO PROGRAMA\n')

#teka de derrota
def loser_panel():
    print('Que pena, você perdeu\n')
    print(f'A palavra era {selected_champion}\n')
    print('FIM DA EXECUÇÃO DO PROGRAMA\n')


define_champion = list(championSelect())
selected_champion = define_champion[0]
tip = define_champion[1]
repeated_letters = []

selected_champion = selected_champion.upper()
word = guess_word()

max_attempts = 6

# execução do programa
while max_attempts > 0:
    hangmanHeader()
    print(f'\nA dica é que a classe desse personagem é {tip}, você tem {max_attempts} tentativas\n')
    print(f'A palavra que você tem que adivinhar é´: {word}')
    missing_letters()
    verify_letter = validate_letter()
    if not check_correct_letter():
        max_attempts -= 1
    if missing_letters() == 0:
        break

if max_attempts > 0:
    hangmanHeader()
    winner_panel()
else:
    hangmanHeader()
    loser_panel()