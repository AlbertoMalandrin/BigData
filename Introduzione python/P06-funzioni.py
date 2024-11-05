def saluta():
    print("ciao")

def somma(a,b):
    s=a+b
    return s

def modifica (m):
    return m+10

saluta()
n=somma(19,20)
print(n)

#i parametri in python son sempre passati per valore (viene sempre fatta una copia), non per indirizzo

print(modifica(n))
print(n)

#l'unico modo di modificare per referenza una variabile è una varibaili in una lista
def modl(ll):
    ll[0]=100

l=[1,2,3]
modl(l)
print(l)

#parametri arbitrari
def f2(*nomi):
    n=len(nomi)
    print("nomi: ", n)
    for n in nomi:
        print(n)

f2("Mario", "Luigi", "Anna")

#parametri default
def saluta2(nome="Mario"):
    print("ciao", nome)

saluta2()
saluta2("Alberto")

#parametri nominali
def assetto(x,y,z):
    print(x,y,z)

assetto(1,2,3)
assetto(z=23, y=12, x=0)

#lambda function (funzioni senza nome)
quadrato=lambda x: x*x
q=quadrato(2)
print(q)

fx=lambda x,y:x*y
print(fx(10,20))

#generatori
def g():
    v=0
    while True:
        yield v
        v += 1

gen=g()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
