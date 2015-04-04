def random_string(randomlen = 8):
	import random, string
	chars = list(string.ascii_letters+string.octdigits)
	for i in range(randomlen):
		yield chars[random.randint(0,len(chars)-1)]
