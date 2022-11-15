def somme_rec(n):
	if n==0:
		return 0
	else :
		return n + somme_rec(n-1)

def somme(n):
	assert (type(n)==int) and (n>=0)
	return somme_rec(n)