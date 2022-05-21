import random

def show_choose_game():

	print('''Choose a game according to the numbers: 
		1. Mega Sena
		2. Quina
		3. Lotofacil
		4. Sair''')

	a = str(input("Game number: "))

	return a

def choose_game(game):
	games = {
		'1': mega,
		'2': quina,
		'3': lotofacil,
		'4': quit
	}

	action = games.get(game)

	return action()

def mega():

	numbers = []

	while True:
		choice = random.randint(1, 60)
		if choice not in numbers:
			numbers.append(choice)

		if len(numbers) == 6:
			break

	numbers.sort()
	return numbers


def quina():

	numbers = []

	while True:
		choice = random.randint(1, 80)
		if choice not in numbers:
			numbers.append(choice)

		if len(numbers) == 5:
			break

	numbers.sort()
	return numbers

def lotofacil():
	numbers = []

	while True:
		choice = random.randint(1, 25)
		if choice not in numbers:
			numbers.append(choice)

		if len(numbers) == 15:
			break

	numbers.sort()
	return numbers

def quit():

	print('Obrigado Por nos escolher. ')
	exit()


while True:
	try:
		print('\n', choose_game(show_choose_game()), '\n')
	except Exception as e:
		print("\n*******Ops Wrong Option********\n\n")
	