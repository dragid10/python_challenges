#edited
PLAYER = 0
POINTS = 1
BET = 2
num_players=int(input('Enter the number of players: '))
#message
print('Maximum number of cards to deal is ' + str(int(52/num_players)) + '.')
num_rounds=int(input('Enter the number of cards to deal: '))

def play_game():
	"""
	starts the game and loops through the turns
	"""
	players = get_players(num_players)
	dealer = get_dealer(players)

	for i in range(0,num_rounds-1):
		players = check_round(players)
		players = play_round(num_rounds-i,players, dealer)
		toString(players)
		dealer = dealer + 1
		if dealer > num_players-1:
			dealer = 0
	for i in range(1,num_rounds+1):
		players = check_round(players)
		players = play_round(i,players,dealer)
		dealer = dealer+1
		toString(players)
		if dealer > num_players-1:
			dealer = 0
	print(players.sort(key=lambda x: int(x[POINTS])))

def get_dealer(players):
	"""
	@params
		List, takes in the list of players and selects the dealer
	"""
	names = []
	for i in range(0,num_players):
		names.append(players[i][PLAYER])
	got_dealer = False
	while not got_dealer:
		name = input('Who is the dealer? ' + str(names))
		for i in range(0,num_players):
			if name == players[i][PLAYER]:
				return i
		print('Dealer not found.')


def check_round(players):
	"""
	@params
		List, takes in the list of players and edits the game as necessary
	"""
	command = input('you can continue(c), edit(e), or stop(s)')
	while command != 'c':
		if command == 's':
			exit()
		if command == 'e':
			for i in range(0,num_players):
				if input('Edit ' + players[i][PLAYER] + '?(y/n) ') == 'y':
					players = edit_player(players, i)
		command = input('you can continue(c), edit(e), or stop(s)')
	return players

def edit_player(players, i):
	"""
	@params
		changes aspects about the player selected
	"""
	if input('is ' + players[i][PLAYER] + ' the correct name?(y/n) ') == 'n':
		players = change_name(players,i)
	if input('is ' + str(players[i][POINTS]) + ' the correct score for ' + players[i][PLAYER] + '?(y/n) ') == 'n':
		players = change_points(players, i)
	if input('is ' + str(players[i][BET]) + ' the correct bet for ' + players[i][PLAYER] + '?(y/n) ') == 'n':
		players = change_bet(players, i)
	return players

def change_points(players, current_player):
	players[current_player][POINTS] = int(input('Previous score was ' + str(players[current_player][POINTS]) + '. New score: '))
	return players

def change_name(players, current_player):
	players[current_player][PLAYER] = input('Enter a new name for ' + players[current_player][PLAYER] + ': ')
	return players

def change_bet(players, current_player):
	players[current_player][BET] = int(input('Previous bet was ' + str(players[current_player][BET]) + '. New bet: '))
	return players

def play_round(cards, players, dealer):
	print(players[dealer][PLAYER] + ' deals ' + str(cards) + ' cards.')
	players = get_bets(players,dealer, cards)
	players = check_round(players)
	players = get_tricks(players)
	return players

def get_bets(players, dealer, cards):
	betting_player = dealer+1
	total_bets = 0
	for i in range(0,num_players):
		if betting_player > num_players-1:
			betting_player = 0
		if i != num_players-1:
			players[betting_player][BET] = int(input('Enter bet for ' + players[betting_player][PLAYER] + ': '))
			total_bets += players[betting_player][BET]
		else:
			print('You cannot bet ' + str(cards-total_bets) + '.')
			players[betting_player][BET] = int(input('Enter bet for ' + players[betting_player][PLAYER] + ': '))
		betting_player += 1
	return players

def get_tricks(players):
	for i in range(0,num_players):
		tricks_taken = int(input('How many tricks did ' + players[i][PLAYER] + ' take?(bet ' + str(players[i][BET]) + '): '))
		if tricks_taken == players[i][BET]:
			players[i][POINTS] += 5+players[i][BET]
		else:
			if players[i][BET] > tricks_taken:
				players[i][POINTS] -= players[i][BET]
			else:
				players[i][POINTS] -= tricks_taken
	return players

def get_players(num):
	players=[]
	for i in range(0,num):
		name = input('Enter the name of player ' + str(i) + ': ')
		players.append([name,0,0])
	return players

def toString(players):
	for i in range(0,num_players):
		print(players[i][PLAYER] + ' has ' + str(players[i][POINTS]) + ' points.')

play_game()
