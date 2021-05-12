import math
import random

#Finder største fælles divisor. Euklids algoritme.
def gcd(x,y):
	while y != 0:
		x, y = y, x%y

	return x

#Tjekker om to tal er indbyrdes prismisk
def is_coprime(x,y):
	return gcd(x,y)==1


#Finder nøglerner E, D og N
def find_noegler(p,q):
	N = p*q #Udregner N (Produkt af de to primtal)
	fi = (p-1)*(q-1)

	#Finder E (Det er et tilfældigt E for sikkerhed)
	E = random.randint(3,fi) 

	while is_coprime(E,fi) != True: #tjekker om de er indbyrdes primisk.
		E = random.randint(3,fi)
	#Finder D. pow er en pythonfunktion, som er mere effektiv end min kode. Den kode, som jeg har skrevet er kommenteret ud nedenfor
	D = pow(E,-1,fi)

	#for i in range(fi):
		#if i>10 and (i*E)%fi==1:
			#D=i
			#break
	

	return E, D, N


p,q = 22187966579491893739746665295613375855031192353526628415949690025789795703311081305968515991008704846576939152182228722315985462593633323507486738480315457,11997521004702871604947399316211057116644036826020074293203137640382109277709740614417085588785015050192182895602973556504501649592195106646002779877165887 #vores to primtal
E,D,N=find_noegler(p,q)

#print(N, "\n")





def tekst_til_tal(tekst): # Denne funktion omdanner teksten til ascii
	tekst = str(tekst)
	return sum(ord(tekst[i])*256**i for i in range(len(tekst)))

def tal_til_tekst(tal): #Denne funktion omdanner ascii tilbage til læsbar tekst og tilføjer det til en list
	tal=int(tal)
	tekst=[]
	while tal != 0:
		tekst.append(chr(tal%256))
		tal//=256
	return "".join(tekst)





#Denne funktion krypterer offentlig_tal
def krypter (tal, E, N):
	return pow(tal, E, N) # dette modul er en optimeret version af (return (tal**E)%N)
	#return (tal**E)%N



#Denne funktion dekrypterer privat_tal
def dekrypter(krypteret_tal,D,N):
	return pow(krypteret_tal, D, N)
	#return (krypteret_tal**D)%N


while  True:
	
	print("Indtast den besked, som du ønsker at kryptere.")
	besked = input(">")
	print("----------------------------------------------------------")
	print("Konverterer til ascii...")

	talbesked=tekst_til_tal(besked)
	print("----------------------------------------------------------")
	print("Krypterer besked...")
	krypteret_talbesked=krypter(talbesked,E, N)
	print("----------------------------------------------------------")
	print("Beskeden er blevet krypteret. Det følgende er den krypterede besked")
	print(tal_til_tekst(krypteret_talbesked))
	input("Tryk enter for at dekryptere.")

	dekrypteret_talbesked=dekrypter(krypteret_talbesked, D, N)
	print("----------------------------------------------------------")
	print("Dekrypterer besked...  Beskeden er hermed dekrypteret")

	print(tal_til_tekst(dekrypteret_talbesked))
	print("----------------------------------------------------------")


	input("Tryk enter for at kryptere en ny besked.")