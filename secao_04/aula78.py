# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

total_question = len(perguntas)
hits = 0
current_question = 0

while current_question < total_question:
    question = perguntas[current_question].get('Pergunta')
    options = perguntas[current_question].get('Opções')
    right_answer = perguntas[current_question].get('Resposta')

    print(f'Pergunta: {question}', end='\n\n')

    if options is not None:
        print('Opções:')
        for index, value in enumerate(options):
            print(f'{index}) {value}')

    response = input('Escolha uma opção: ')
    is_right = False

    if response.isdigit():
        response_int = int(response)
        if response_int >= 0 and response_int < len(options):
            if right_answer == options[response_int]:
                hits += 1
                is_right = True

    if is_right:
        print('Acertou ✅', end='\n\n')    
    else: 
         print('Errou 💩', end='\n\n')

    current_question += 1

print(f'Você acertou {hits}')
print(f'de {total_question} perguntas')