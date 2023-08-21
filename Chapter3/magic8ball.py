import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'É certeza.'
    elif answerNumber == 2:
        return 'Provavelmente sim.'
    elif answerNumber == 3:
        return 'Sim.'
    elif answerNumber == 4:
        return 'Pergunta não clara, tente novamente.'
    elif answerNumber == 5:
        return 'Pergunte novamente mais tarde.'
    elif answerNumber == 6:
        return 'Concentre-se e pergunte novamente.'
    elif answerNumber == 7:
        return 'Minha resposta é não.'
    elif answerNumber == 8:
        return 'Não posso garantir isso.'
    elif answerNumber == 8:
        return 'Duvido muito'

input("Digite o que você deseja saber: ")
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

# print(getAnswer(random.randint(1, 9)))