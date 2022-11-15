def puiss(x,n) :
	if n == 0 :
		return 1
	elif n%2 == 0 :
		return puiss(x,n//2)**2
	else :
	return x*puiss(x,(n-1)//2)**2