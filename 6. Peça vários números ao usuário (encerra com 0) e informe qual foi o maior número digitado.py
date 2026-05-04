n = int(input("Digite um número: "))
m=0
while n!=0:
	if(n>m):
		m=n
	n=int(input("Digite um número: "))
print("Maior número", m)
