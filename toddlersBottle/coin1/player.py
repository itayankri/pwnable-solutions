#!/usr/bin/env python

import socket
import time

# *********************************************
# *** Run This script on pwnable.kr servers ***
# *********************************************


# A function that searches for a counterfeit coin in a range of coins.
def findCoin(start, end, chances, sock):
	if chances == 0:
		if start + 1 == end:
			print "The counterfeit coin is coin number " + str(start)
		else:
			print "Failed to find coin: start = " + str(start) + " end = " + str(end)
			quit()

	# Calculate the amount of coins that we have.	
	coinsNumber = end - start

	# Calculate the size of the lowe half.
	halfPoint = (end + start) / 2 + (coinsNumber % 2 == 1)

	# Construct a string that represents the guess message.
	guess_message = ""
	for i in range(start, halfPoint):
		guess_message += str(i) + " "
	
	# print "Guess: " + guess_message
	guess_message += '\n'

	# Send the guess message to the game service.
	sock.send(guess_message)
	
	if chances >= 9:
		time.sleep(0.1)

	# Recieve the weight of the coins that we weighed.
	# print "Result: ",
	result = sock.recv(13)
	if 'Correct!' in result:
		print result
		return

	# If the weight is a multiply of 10, search the coin in the higher half.
	# Else, search the coin in the lower half.
	if int(result) % 10 == 0:
		findCoin(halfPoint, end, chances - 1, sock)
	else:
		findCoin(start, halfPoint, chances - 1, sock)


TCP_IP = '127.0.0.1'
TCP_PORT = 9007
BUFFER_SIZE = 1024
instructions_message_size = 1102
game_variables_message_size = 11

# Create a socket which will communicate with the game service.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Initialize a TCP handshake with the game service.
s.connect((TCP_IP, TCP_PORT))

# Recieve the first message from the server.
instructions_message = s.recv(instructions_message_size)

for i in range(100):
	print "\n*** Round #" + str(i) + " ***\n"
	# Recieve the 'N=<number> C=<number>' message.
	time.sleep(0.1)
	game_variables = s.recv(game_variables_message_size)
	print game_variables

	# Parse the variables message and convert the strings to numerical values.
	coins = int(game_variables.split(' ', 1)[0].split('=', 1)[1])
	chances = int(game_variables.split(' ', 1)[1].split('=', 1)[1])

	print "coins: " + str(coins) + " chances: " + str(chances) + "\n"

	findCoin(0, coins, chances, s)

time.sleep(0.2)
flag = s.recv(BUFFER_SIZE)

print "The flag is: " + flag

s.close()

