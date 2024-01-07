while True:
	try:
		t, v = map(int, input().split(' '))
		print(v*t*2)
	except EOFError:
		break
