import maksimum as cdb

def test_maksimum():
	lista=[1,3,2,5,3,4,2]
	assert (cdb.maksimum(lista) == max(lista))
