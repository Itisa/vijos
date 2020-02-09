###FBI tree

a = int(input())
b = input()
ans = ''
x = a
def fbi(a):
	if '1' in a and '0' in a:
		return 'F'
	elif '1' in a:
		return 'I'
	else:
		return 'B'

def spli(string):
	l = len(string)
	le = l[:l/2]
	lr = l[l/2:]
	return le,lr

def if_2(num):
	i = 0
	for x in range(10):
		if num%2 != 0:
			return i
		num = num/2
		i += 1
		if num==1:
			return i
def muli(num,m):
	r = 1
	for i in range(m):
		r = r*num
	return r

x += 1
n = [0]
for i in range(len(b)):
	ans += fbi(b[i])
	t = if_2(i+1)

	for i1 in range(t):
		loc = i+1
		move = muli(2,i1+1)
		ans += fbi(b[loc-move:loc]) 
	
print(ans)