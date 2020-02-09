	# k = int(input())

import time
t0 = time.time()

def get_yin(num):
	r = 0
	for i in range(1,num+1):
		if num%(i)==0:
			r += 1
	return r
def get(num):
	k = num
	if_find = False
	for i in range(1,20001):
		n = get_yin(i)
		# for i1 in range(1,i+1):
			# if i%(i1)==0:
				# n += 1
		if n == k:
			return i
			break
			if_find = True
	if not if_find:
		return "NO SOLUTION"
		print("NO SOLUTION")

# ans = {}
# for i in xrange(60,61):
# 	n = get(i)
# 	ans[i] = n
# print(ans)
t1 = time.time()

print(t1-t0)
# {1: 1, 2: 2, 3: 4, 4: 6, 5: 16, 6: 12, 7: 64, 8: 24, 9: 36, 10: 48, 11: 1024, 12: 60, 13: 4096, 14: 192, 15: 144, 16: 120, 17: 'NO SOLUTION', 18: 180, 19: 'NO SOLUTION', 20: 240, 21: 576, 22: 3072, 23: 'NO SOLUTION', 24: 360, 25: 1296, 26: 12288, 27: 900, 28: 960, 29: 'NO SOLUTION', 30: 720, 31: 'NO SOLUTION', 32: 840, 33: 9216, 34: 'NO SOLUTION', 35: 5184, 36: 1260, 37: 'NO SOLUTION', 38: 'NO SOLUTION', 39: 'NO SOLUTION'}
# {41: 'NO SOLUTION', 42: 2880, 43: 'NO SOLUTION', 44: 15360, 45: 3600, 46: 'NO SOLUTION', 47: 'NO SOLUTION', 48: 2520, 49: 'NO SOLUTION'}
# {51: 'NO SOLUTION', 52: 'NO SOLUTION', 53: 'NO SOLUTION', 54: 6300, 55: 'NO SOLUTION', 56: 6720, 57: 'NO SOLUTION', 58: 'NO SOLUTION', 59: 'NO SOLUTION'}
# {64: 7560, 65: 'NO SOLUTION', 66: 'NO SOLUTION', 67: 'NO SOLUTION', 68: 'NO SOLUTION', 69: 'NO SOLUTION', 70: 'NO SOLUTION', 71: 'NO SOLUTION', 72: 10080, 73: 'NO SOLUTION', 74: 'NO SOLUTION', 75: 'NO SOLUTION', 76: 'NO SOLUTION', 77: 'NO SOLUTION', 78: 'NO SOLUTION', 79: 'NO SOLUTION', 61: 'NO SOLUTION', 62: 'NO SOLUTION', 63: 14400}
# {80: 15120}

answers = {1: 1,
 2: 2,
 3: 4,
 4: 6,
 5: 16,
 6: 12,
 7: 64,
 8: 24,
 9: 36,
 10: 48,
 11: 1024,
 12: 60,
 13: 4096,
 14: 192,
 15: 144,
 16: 120,
 17: 'NO SOLUTION',
 18: 180,
 19: 'NO SOLUTION',
 20: 240,
 21: 576,
 22: 3072,
 23: 'NO SOLUTION',
 24: 360,
 25: 1296,
 26: 12288,
 27: 900,
 28: 960,
 29: 'NO SOLUTION',
 30: 720,
 31: 'NO SOLUTION',
 32: 840,
 33: 9216,
 34: 'NO SOLUTION',
 35: 5184,
 36: 1260,
 37: 'NO SOLUTION',
 38: 'NO SOLUTION',
 39: 'NO SOLUTION',
 41: 'NO SOLUTION',
 42: 2880,
 43: 'NO SOLUTION',
 44: 15360,
 45: 3600,
 46: 'NO SOLUTION',
 47: 'NO SOLUTION',
 48: 2520,
 49: 'NO SOLUTION',
 51: 'NO SOLUTION',
 52: 'NO SOLUTION',
 53: 'NO SOLUTION',
 54: 6300,
 55: 'NO SOLUTION',
 56: 6720,
 57: 'NO SOLUTION',
 58: 'NO SOLUTION',
 59: 'NO SOLUTION',
 50: 6480,
 40: 1680,
 60: 5040,
 80: 15120,
 64: 7560,
 65: 'NO SOLUTION',
 66: 'NO SOLUTION',
 67: 'NO SOLUTION',
 68: 'NO SOLUTION',
 69: 'NO SOLUTION',
 70: 'NO SOLUTION',
 71: 'NO SOLUTION',
 72: 10080,
 73: 'NO SOLUTION',
 74: 'NO SOLUTION',
 75: 'NO SOLUTION',
 76: 'NO SOLUTION',
 77: 'NO SOLUTION',
 78: 'NO SOLUTION',
 79: 'NO SOLUTION',
 61: 'NO SOLUTION',
 62: 'NO SOLUTION',
 63: 14400}

########################################################
def get_su():
	a = [2,3,5]
	for i in range(5,150):
		su = 0
		for i1 in a:
			if i%i1==0:
				su = 1
				break
		if su == 0:
			a.append(i)
	return a
a = get_su()

k = 42


def cal_n(sus):
	su = sus[:]
	s = []
	while len(su) != 0:
		num = su[0]
		n1 = su.count(num)
		s.append(n1+1)

		for i in range(n1):
			su.pop(0)
	n = 1
	for i in s:
		n *= i
	return n
def main(k):
	for i in range(1,20002):
		if i == 20001:
			# print("NO SOLUTION")
			return "NO SOLUTION"
			break
		num = i
		n = 0
		sus = []
		while num != 1:

			for i1 in a:
				if num %i1 == 0:
					num /= i1
					sus.append(i1)
					break
				if i1 == 149:
					num = 1
					sus = [num]

		n = cal_n(sus)
		if n == k:
			# print(i)
			return i
			break
for i in range(1,81):
	r = main(i)
	if not answers[i] == r:
		print(i,r,answers[i])		 
	
