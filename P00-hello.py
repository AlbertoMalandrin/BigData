print("Hello Python")#stampo un messaggio
print('ciao python')     

#commenti
'''
Un testo
su più
righe
'''
#variabili
temp_stanza=12.0
nome='Mario'
test=True
n=100

print(n)

m=n+20
# + - * / , ** elevamento a potenza, % modulo
print(m)

tuo_nome=input("Dammi il tuo nome: ")
print("Il tuo nome è dunque: " + tuo_nome)
print("Il tuo nome è dunque: ", tuo_nome)

#template e stringhe
print(f"Ciao, {tuo_nome}")

#operatori e stringhe
msg="ciao"+tuo_nome+'!'
print(msg)

numero=input("Dammi un numero: ")
calcolo=int(numero)*2
print(calcolo)

#int() str()