lista=[2,5,3,4,1,3,6,1]
def maksimum(lista):
	maks=lista[0]
	dl=len(lista)
	for i in range(dl):
		if(lista[i]>maks):
			maks=lista[i]
	return maks
