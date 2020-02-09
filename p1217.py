rate = ''
while True:
	i = input()
	rate+=i
	if 'E' in i:
		break
	if rate == '' and i == '':
		rate = 'E'
		break
def match(r,win=11):
	ans = ''
	w = 0
	l = 0
	for i in range(len(r)):
		if r[i] == 'W':
			w += 1
		elif r[i] == 'L':
			l += 1
		elif r[i] == 'E':
			return (w,l,i,'c')

		if w >= win and w-l >= 2:
			return (w,l,i,'e')
		elif l >= win and l-w >= 2:
			return (w,l,i,'e')
r11 = []
ra = rate
while 'E' in ra:
	w1,l1,i1,s1 = match(ra)
	r11.append([w1,l1])
	ra = ra[i1+1:]
	if s1 == 'e' and ra == '':
		r11.append([0,0])

r21 = []
ra = rate

while 'E' in ra:
	w1,l1,i1,s1 = match(ra,21)
	r21.append([w1,l1])
	ra = ra[i1+1:]
	if s1 == 'e' and ra == '':
		r21.append([0,0])
	

for i in r11:
	print('%s'%i[0]+':'+'%s'%i[1])
print('')
for i in r21:
	print('%s'%i[0]+':'+'%s'%i[1])

