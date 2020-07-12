hex_flag = ['2e585055', '203f2e2e', '6e756f73', '6c207364', '20656b69', '65642061', '6576696c', '73207972', '69767265', '3a206563', '00000029']

for word in hex_flag:
	print(bytes.fromhex(word).decode('utf-8')[::-1], end="")

print()
