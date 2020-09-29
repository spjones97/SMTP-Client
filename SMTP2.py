import sys

#path = sys.argv[1]Z
#forward = open(path)
#sender = forward.readline()

def whitespace(string, index):
	if (string[index] != ' ' and string[index] != '\t'):
		return 1
	index = index + 1
	while (index < len(string)):
		if (string[index] == ' ' or string[index] == '\t'):
			index += 1
		else:
			return index

def check250(string):
	err = string.lower()
	if (string[0:3] != "250"):
		return 1
	index = whitespace(err, 3)
	if (index == 1 or string[index] == '\n'):
		return 1
	return 0

def check354(string):
	err = string.lower()
	if (string[0:3] != "354"):
		return 1
	index = whitespace(err, 3)
	if (index == 1 or string[index] == '\n'):
		return 1
	return 0


while  True:
	path = sys.argv[1]
	forward = open(path)
	sender = forward.readline()

	sys.stdout.write("MAIL FROM:" + sender[5:len(sender)])

	msg = sys.stdin.readline()
	sys.stderr.write(msg)
	if (check250(msg) == 1):
		print("QUIT")
		sys.exit(1)

	receiver = forward.readline()
	while (receiver[0:3] == "To:"):
		sys.stdout.write("RCPT TO:" + receiver[3:len(receiver)])

		msg = sys.stdin.readline()
		sys.stderr.write(msg)
		if (check250(msg) == 1):
			print("QUIT")
			sys.exit(1)
		receiver = forward.readline()

	print("DATA")

	msg = sys.stdin.readline()
	sys.stderr.write(msg)
	if (check354(msg) == 1):
		print("QUIT")
		sys.exit(1)

	another = False
	if (receiver[0:5] != "From:"):
		sys.stdout.write(receiver)

		for line in forward:
			if (line[0:5] == "From:"):
				sender = line
				another = True
				break
			else:
				sys.stdout.write(line)
	else:
		another = True

	print('.')

	msg = sys.stdin.readline()
	sys.stderr.write(msg)
	if (check250(msg) == 1):
		print("QUIT")
		sys.exit(1)

	if (not another):
		print("QUIT")
		sys.exit(0)
print("QUIT")
sys.exit(0)
