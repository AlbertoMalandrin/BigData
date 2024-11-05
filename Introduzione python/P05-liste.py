#liste

numeri=[1,2,45,67,89,3]
print(len(numeri))
print(numeri[0])
numeri[4]=99
print(numeri)
print(numeri[0:3])
print(numeri[3:])
print(numeri[-1])

giorni=['lun', 'mar', 'mer', 'gio', 'ven']
print(giorni.count('gio'))
giorni.append('gio')#aggiunge in fondo
print(giorni)
print(giorni.count('gio'))
print('lun' in giorni) #ritorna booleano
print(giorni.index('mar'))
giorni.remove('ven')
print(giorni)
#giorni.remove('dom')
#print(giorni)
print(giorni.pop()) #elimina ultimo elemento e te lo restituisce
print(giorni)

#le stringhe sono particolari tipi di array
nome="Mario"
print(nome[2])
print(len(nome))
print(nome[2:4])

#tuple (lista non modificabile)
costanti=('abc', 'pass', 'ssid')
print(len(costanti))
print(costanti[1])

#set ossia insiemi, non garntisce l'ordine e non ammette duplicati
s1={'A', 'B', 'C'}
s1.add('D')
print(s1)#quando ristampo l'ordine cambia
s1.add('D')
print(s1)#quando ristampo non c'è duplicato di D
print(len(s1))

#frozen set (set non modificabile)
s2=frozenset(['A', 'B', 'C'])
print(s2)

#dizionario, coppia chiave valore
telefoni={'mario':'34466', 'luigi':'47385873'}
print(telefoni)
telefoni['giovanni']='73247'#aggiungere coppia chiave valore
print(telefoni)

for k in telefoni.keys():
    print(k, end=' ')

for v in telefoni.values():
    print(v, end=' ')

print("\n")
for k in telefoni.keys():
    print(telefoni[k], end=' ')

#list comprension0
print("\n")
ll=[i*2 for i in range(0,10)]
print(ll)

print("\n")
ll2=[i**2 for i in range(0,10)]
print(ll2)

