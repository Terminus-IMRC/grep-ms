#!/usr/bin/env python3
import math, sys

common_sum=None

def error(str, exitcode=1):
	print(sys.argv[0] + ": error: " + str, file=sys.stderr)
	exit(exitcode)

def check_all_unique(s, Ceilings):
	for i in range(0, Ceilings):
		for j in range(i+1, Ceilings):
			if s[i]==s[j]:
				return False
	return True

def check_vertical_sums(s, X):
	global common_sum
	for i in range(X):
		sum=0
		for j in range(X):
			sum+=s[i+j*X]
		if common_sum==None:
			common_sum=sum
		elif sum!=common_sum:
			return False
	return True

def check_horizontal_sums(s, X):
	global common_sum
	for i in range(X):
		sum=0
		for j in range(X):
			sum+=s[i*X+j]
		if common_sum==None:
			common_sum=sum
		elif sum!=common_sum:
			return False
	return True

def check_diagonal_sums(s, X):
	global common_sum
	sum_rt=0
	sum_lt=0
	for i in range(X):
		sum_rt+=s[(X-i-1)+i*X]
		sum_lt+=s[i+i*X]
	if sum_rt!=sum_lt:
		return False
	if common_sum==None:
		common_sum=sum_rt
	return True

def main():
	while True:
		try:
			s=input()
		except EOFError:
			break

		ss=[int(i) for i in s.split()]
		if math.modf(math.sqrt(len(ss)))[0]!=0:
			error("invalid length of input line")
		Ceilings=len(ss)
		X=int(math.sqrt(Ceilings))

		if_uniq=check_all_unique(ss, Ceilings)
		if_v=check_vertical_sums(ss, X)
		if_h=check_horizontal_sums(ss, X)
		if_d=check_diagonal_sums(ss, X)

		if if_uniq and if_v and if_h and if_d:
			print(s)

if __name__=='__main__':
	main()
