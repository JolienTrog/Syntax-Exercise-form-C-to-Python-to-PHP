#Python Crashkurs

### Datentypen
## Int
1, 2, 43

## Floats mit Punkt geschrieben
1.2, 100.4

## String
# mit '' oder "" best practice ""
"hello"

## Booleans
# first letter uppercase

True, False

## Variablen 
# können überschrieben werden
x = 1
#x = "hello"
y = 1.3
#neue zeile am ende
print(x, y) 

#keine neue Zeile sondern hintereinander mit end, variablen trennen mit sep
#int und float können gerechnet werden, mit string und int nicht
print(x, y, end="|", sep="- ")

z = x + y
print(z)

# string + string können addiert werden
a = "Hallo"
b = "Du"
c = a + b
print(c)

b1 = True
b2 = False
b3 = b1 + b2
print(b3)
# ergebnis ist 1 weil false = 0, true = 1 werden zusammen addiert
# bool können auch mit int und floats addiert werden

### Vergleichsoperatoren
#== gleich
#!= ungleich
#<= größer gleich
#< größer
# usw.

#mehrere Werte vergleichen, beide müssen true sein
print(x > y and y > z)
#ist das gleiche wie
print(x > y > z)

#Werte gegeneinander vergleichen, nur eine muss true sein
print(x > y or y > z)

# and und or in einem, wird and zuerst geprüft, dann or
print(x > y or (z > y and z > x))

#Input
#x = input("Erste Zahl ")
#y = input("Zweite Zahl ")
print(x + y)
# x = 5, y = 5
# ergebnis ist 55 da input als string gelesen wird und zahlen konkatinated werden

# mit int wird es als zahl gelesen
#x = int(input("Erste Zahl "))
#y = int(input("Zweite Zahl "))
print(x + y)

#Verzweigungen
x = 12
y = 50
z = 100

if x > 50:
    print("yes")
elif x >= 100 and x < 90:
    ("mayby")
else:
    print("no")
#code wird von oben nach unten ausgeführt, dies muss bei Bedingungen beachtet werden


# Iterables
### List
# mutable = Variablen können neue Werte zugewiesen werden
x = [10, True, "hello"]
print(x[0])
# ersten Wert ausgeben
# "indexError: list index out of range" bedeutet das Wert größer als Liste ist

#gibt element 0 bis 1 excluded 1
print(x[0:1])

#wenn von 0 ab ausgegeben werdne soll
print(x[:3])
# ab index bis ende
print(x[3:])
# letztes Element aus liste
print(x[-1])
# step size, zb. nur jedes 2. Element, mit Wert an 3. Stelle
print(x[1:5:2])
#liste verkehrt herum anzeigen
print(x[::-1])

### Tuble
# nicht mehr veränderbar!!!
# immutable
y = (1, 2, True)

### Set
# nur unique Werte
# kein Index!! (keine feste Reihnfolge)
# immutable
z = {1, "hallo", 5.5, "hallo"}

###Schleifen 
# for-loop
x = {1, 555, 3, 4} 

for item in x:
    if item == 4:
        print(item + 10)
    else:
        continue
        #break

#mit Index durch enumerate
for index, item in enumerate(x):
    print(index, item)

#output: 
# 0 1
# 1 3
# 2 4
# 3 555

### while-loop
#variable als index wert muss am anfang initialisiert werden und iteriert
i = 0

while i < 3:
    print(x[i])

#Endlosschleife
while True:
    print("endless")


#Variable in output
print(f"Das ist der Variablenwert{i}")

#Object und Methods
# in Python ist alles ein Objekt!!