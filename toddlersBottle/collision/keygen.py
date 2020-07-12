#!/usr/bin/python3.6

import random

def check_key(key):
	char_sum = 0

	for i in range(5):
		char_sum = char_sum << 2
		part = "".join("{:02x}".format(ord(c)) for c in key[i*4:(i+1)*4])
		char_sum += int(part, 16)
		
		if len(hex(char_sum)) > 10:
			#print("Dropped " + hex(char_sum)[2] + " from " + hex(char_sum))
			char_sum = int(hex(char_sum)[3:], 16)
			#print("New " + hex(char_sum))
	return char_sum

while True:
	key = ""
	for i in range(20):
		key += random.choice("abcdefghizklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_+`\"\\':;<,>.?/")

	s = check_key(key)
	if s == 0x21dd09ec:
		print("Found a valid key - " + key)
		exit()
	else:
		print(key + " | " + hex(s) + " | " + str(s))
