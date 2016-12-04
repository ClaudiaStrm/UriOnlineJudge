
i, j = 1, 60

while j >= 0:
	print('I=%d J=%d' %(i, j))
	j -= 5
	i += 3


i, j = 1, 7

while i <= 9:
	while j >= 5:
		print('I=%d J=%d' %(i, j))
		j -= 1
	i += 2
	j = 7


i, j = 1, 7
k = j - 2

while i <= 9:
	while j >= k:
		print('I=%d J=%d' %(i, j))
		j -= 1
	k = j + 3
	i += 2
	j += 5



i, j = 0, 1

while i <= 1.8:
	for x in range(0,3):
		if i == 0 or i - 1 == 0.0 or i - 2 == round(0.0):
			print('I=%d J=%d' %(i, j))
		else:
			print('I=%.1f J=%.1f' %(i, j))
		j += 1
	j -= 2.8
	i += 0.2
j = 3
i = 2
for x in range(0,3):
	print('I=%d J=%d' %(i, j))
	j+=1
	