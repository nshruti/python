f = open('datagen.csv')
tot,n = 0,0 
for row in f:
	n+= 1
	numbers=int(row.split(',')[2][1:-2])
	if numbers > 100000:
		print numbers
	tot+=numbers
	#tot+= int(row.split(',')[2][1:-2])
print tot,n,tot/n