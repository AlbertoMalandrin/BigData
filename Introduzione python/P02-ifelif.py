voto = int(input("dammi un voto (da 1 a 10): "))
if voto >= 8:
    print("ottimo")
elif voto >= 6:
    print("sufficiente")
else:
    print("insufficiente")
print("end")

#operatore ternario
n=int(input("inserisci n: "))
print("MAGGIORE 10") if (n>10) else print("MINORE 10")
print("PARI") if (n%2)==0 else print("DISPARI")
