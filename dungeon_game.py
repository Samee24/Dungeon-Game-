import random

#Our grid - can be expanded but wanted to keep it simple
CELLS = [(0,0), (0,1), (0,2),
	 (1,0), (1,1), (1,2),
	 (2,0), (2,1), (2,2)]

#Initial position assignments
def set_position(monster, person, door):
	temp = CELLS[:]
	monster = random.choice(temp)
	temp.remove(monster)
	person = random.choice(temp)
	temp.remove(person)
	door = random.choice(temp)

	return monster, person, door

#Actally move the player
def player_move(move, person):
	x = 0
	y = 0
	x, y = person

	if (move == 'LEFT'):		
<<<<<<< HEAD
		person = x, y - 1
	elif(move == 'RIGHT'):
		person = x, y + 1
	elif(move == 'UP'):
		person = x - 1, y
	elif(move == 'DOWN'):
		person = x + 1, y
=======
	   person = x - 1, y
	elif(move == 'RIGHT'):
	   person = x + 1, y
	elif(move == 'UP'):
	   person = x, y + 1
	elif(move == 'DOWN'):
	   person = x, y - 1
>>>>>>> 21c90ad239dd257d818fbdb6b2759a00609a28c5
	else:
	   print("error")
	return person
	
#The possible locations a user can move
def checkavailable_moves(person):
	moves= ["LEFT", "RIGHT", "UP", "DOWN"]
	x, y = person
	if x == 0:		
<<<<<<< HEAD
		moves.remove("UP")
	if y == 0:
		moves.remove("LEFT")
	if x == 2:
		moves.remove("DOWN")
	if y == 2:
		moves.remove("RIGHT")

	return moves

def draw_map(player):
	for cell in CELLS:
		if cell[1] == 2:
			if cell == player:
				print('      ___X___')
			else:
				print('      _______')
		else:
			if cell == player:
				print('      ___X___      ', end = '')
			else:
				print('      _______      ', end = '')


=======
	   moves.remove("LEFT")
	if y == 0:
	   moves.remove("DOWN")
	if x == 2:
	   moves.remove("RIGHT")
	if y == 2:
	   moves.remove("UP")
	return moves

>>>>>>> 21c90ad239dd257d818fbdb6b2759a00609a28c5
def welcome():
   print("Welcome to my dungeon! Mwahahahaha.")
   print("Enter left, right, up or down. Type QUIT to quit.")

def init():
    monster, person, door = set_position(CELLS)

welcome()
monster = tuple()
person = tuple()
door = tuple()
monster, person, door = set_position(monster, person, door)
print("\nMONSTER IS AT {}".format(monster))

while True:
	print("\nYou're currently at {}".format(person))
	moves_avail = checkavailable_moves(person)
	print("You can move {}".format(moves_avail))

	move = input("Enter move! ")
	move = move.upper()

	if move == 'QUIT':
	   break

	if move not in moves_avail:
	   print("Please enter a valid move!")
	else:		
<<<<<<< HEAD
		person = player_move(move, person)

		if person == monster:
			print("The monster got you. You lost!")
			break
		elif person == door:
			print("You escaped! Hell yeah!!!")
			break
	draw_map(person)
=======
	   person = player_move(move, person)
	   if person == monster:
	      print("The monster got you. You lost!")
	         break
	   elif person == door:
	      print("You escaped! Hell yeah!!!")
	         break
>>>>>>> 21c90ad239dd257d818fbdb6b2759a00609a28c5







