import random

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def askForGuess():
    while True:
        guess = input('> ')

        if guess.isalpha():
            return guess.upper()
        print('Por favor informe uma letra entre A e Z')

print('Adivinhe a Letra, por Thai Moraes')
print()
secretLetter = random.choice(alphabet)
print('Estou pensando numa letra entre A e Z')

for i in range(10):
    print('Você possui {} tentativas. Tente adivinhar a letra!'.format(10-i))

    guess = askForGuess()

    if guess == secretLetter:
        break

    if guess < secretLetter:
        print("Sua tentativa é MENOR em ordem alfabética")
    if guess > secretLetter:
        print("Sua tentativa é MAIOR em ordem alfabética")

if guess == secretLetter:
    print("Yay! Você adivinhou a letra!")
else:
    print("Fim de jogo. A letra que eu estava pensando era", secretLetter)