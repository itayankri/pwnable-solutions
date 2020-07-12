#!/usr/bin/env python

# This is the most unstable script in the world, but it worked once, so it was enough.

import socket
import time
import os

os.system("clear")

TCP_IP = '127.0.0.1'
TCP_PORT = 9009
BUFFER_SIZE = 1024
cash = 500 

def calcBet(m, d, cash):
	if (d == 1  or d == 11) and m != 1 and m != 11:
		return 0

	if d * (21 / m) > m * (21 / m) and d * (21 / m) <= 21:
		return 0
	else:
		return cash

# A function that creates a HIT string according to the given
# card value.
def play2(my_card, dealers_card):
	global cash
	bet = str(calcBet(my_card, dealers_card, cash)) + "\n"
	print "Bet: " + bet + "\n"
	if bet == 0:
		return bet + "s\n"

	cash *= 2

	# If the value is 11 (which means that card is an Ace),
	# we need10 more Aces to win.
	if my_card == 11:
		return bet + "h\nh\nh\nh\nh\nh\nh\nh\nh\nh\n"
	if my_card == 1:
		return bet + "h\nh\nh\nh\nh\nh\nh\nh\nh\nh\nh\nh\nh\nh\nh\nh\nh\nh\nh\nh\n"
	else:
	        hits = ""
		# Calculate the number of times we need to hit in
		# in order to win.
        	n = (21 / my_card) - 1
		
		# Concatenate 'h\n' N times.
        	hits += "h\n" * n
    
		# If the HIT message does not take us to 21 exactly,
		# concatenate an 's\n' in order to stop the round.
	        if 21 % my_card != 0:
        	        hits += "s\n"

    		# Return the HIT string.
	        return bet + hits

def play(my_card, dealers_card):
	global cash
	bet = str(calcBet(my_card, dealers_card, cash)) + "\n"
        print "Bet: " + bet + "\n"

	if bet == 0:
                return bet + "s\n"

	if (21 / my_card) >= 3 and dealers_card == 7:
		return "0\ns\n"

	for i in range(my_card * (21 / my_card) + 1, 22):
		if i % dealers_card == 0:
			return "0\ns\n"	

        cash *= 2
	return bet + "h\n" * ((21 / my_card) - 1) + "s\n"

# Create a socket which will communicate with the game service.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Initialize a TCP handshake with the game service.
s.connect((TCP_IP, TCP_PORT))

# Recieve the first screen.
time.sleep(1)
s.recv(1822)

# Send 'Y' in order to move to the second screen.
s.send("Y\n")

# Recieve the second screen.
time.sleep(0.5)
s.recv(150)

# Send '1' in order to start the game.
s.send("1\n")

for i in range(20):
	# Recieve The initial state screen.
	time.sleep(0.15)
	first_card_screen = s.recv(125)
	if "You Are Bankrupt. Game Over" in first_card_screen:
		print "Player failed, improve the algorithm"
		quit()
	else:
		print str(len(first_card_screen)) 
		print first_card_screen.split('\n')
	card_value = int(first_card_screen.split('\n')[8].split(' ')[3])
	dealers_card = int(first_card_screen.split('\n')[10].split(' ')[6])

	print "Card Value: " + str(card_value)
	print "Dealer's Card: " + str(dealers_card)


	# Send a bet with a HIT message.
	move = play(card_value, dealers_card)
	print ">> Move: " + move
	s.send(move)

	# Recieve the response.
	time.sleep(1)
	print "<< Recieved: " + s.recv(1024*4)

	# Send 'Y' in order to start another game.
	print ">> Sent 'Y'"
	s.send("Y\n")

