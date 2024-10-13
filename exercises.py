#!/usr/bin/python
# -*- coding: latin-1 -*-

# name = "Ale"
# age = 36
# weight = 81.05

# print("Il mio nome è %s ed ho %d anni. Il mio peso è %.2f" % (name, age, weight))

# print("Il mio gatto si chiama {name}, ha {age}, anni e pesa {weight}kg".format(name=name, age=age, weight=weight))

# # print(f"Il mio gatto si chiama {name}, ha {age}, anni e pesa {weight}kg") questa non funziona #

# my_list = [0,5,3,6,8]

# print(type(my_list))

# print(my_list[:1:-1])

# my_list[-2:] = [0,0]

# print(my_list)

# animals = ["gatto", "mucca", "gallina"]

# print("toro" in animals)

# items = {"cereali": 2, "uva": 3, "sapone": 4}

# print(list(items.keys()))

# items["yogurt"] = {"fragola": 2, "mango": 1}

# print(list(items.keys()))

# print(items["yogurt"])

# myset = {"pino", "giancarlo", "miriam", "giancarlo"}

# print(myset)

# myset.add("nino")

# print(myset)

# mylist = [7,4,6,5,3,]

# mylist.insert(2, "qui")

# print(mylist)

# n = int(input("Dimmi fino a che numero stampare: "))

# for i in range(0, n):
#   print(i)

# print("fine")

# FIBONACCI OLD SCHOOL

# n = int(input("Quanti num di fubonacci vuoi?"))

# first_fib = 0

# second_fib = 1

# for i in range(0, n):
#     next_fib = first_fib+second_fib
#     first_fib = second_fib
#     second_fib = next_fib
#     print(first_fib)

# FIBONACCI NEW SCHOOL

# n = int(input("Quanti num di fubonacci vuoi?"))

# first_fib = 0

# second_fib = 1

# for i in range(0, n):
#     print(second_fib)
#     first_fib,second_fib = second_fib, second_fib+first_fib

# ITERAZIONE sull'indice

lista = ["tofu", "yogurt greco", "latte", "farina"]
# for i in range(0, len(lista)):
#   print("%d) %s" % (i, lista[i]))

# ITERAZIONE sulla lista

# for i, cibi in enumerate(lista):
#   print("-%d %s" % (i, cibi))

# COSA SUCCEDE
# for cibi in enumerate(lista):
#   print(cibi)
# i = 1
# n = input("fino a quanto?")

# while i<n:
#   if i%3==0:
#       i+=2
#       continue
#   print(i)
#   i+=2

# PROGRAMMAZIONE AD OGGETTI

# class Triangle():
#   def __init__(self, a,b,c,h):
#     self.a, self.b, self.c, self.h = a,b,c,h
  
#   def area(self):
#     return self.b*self.h/2

#   def perimeter(self):
#     return self.a+self.b+self.c

#   def info(self):
#     print("Il triangolo ha un'area di %.2f" % (self.area()))
#     print("Il triangolo ha un perimetro di %.2f" % (self.perimeter()))

# myTriangle = Triangle(4,3,8,5)

# myTriangle.info()

# help(myTriangle)

"""
Scrivi un programma che chieda due numeri all'utente tramite la funzione input e mostri il più grande tra i due utilizzando la funzione print.
Per quanto Python disponga di una funzione max(), siete invitati ad utilizzare le istruzioni istruzioni if, elif ed else per la scrittura dell'algoritmo.
"""

# a = input("Enter a number")
# b = input("Enter a second number")

# if a>b:
#   print("The number %.2f is greater than %.2f." % (a,b))
# elif b>a:
#   print("The number %.2f is greater than %.2f." % (b,a))
# else:
#   print("The numbers are the same.")

"""
Scrivi un programma che chieda tre numeri a, b, c all'utente e mostri il più grande tra loro.
"""
# a = input("Enter a number")
# b = input("Enter a second number")
# c = input("Enter a third number")

# if a >= b and a >= c:
#     print(a)
# elif b >= a and b >= c:
#     print(b)
# elif c >= a and c >= b:
#     print(c)

"""
Scrivi un programma che, data una lista di numeri, fornisca in output il maggiore tra tutti gli elementi della lista.
"""

# numbers = [-1, 3, 15, 30, 45, 60, 2]
# greater = 0
# for number in numbers:
#   if greater < number:
#     greater = number
# print("The greater number is %d" % greater)

"""
Scrivi un programma che chieda all'utente una stringa composta da un solo carattere e dica se si tratta di una vocale oppure no.
"""

# letter = input("Enter a letter: \n")

# if letter.lower() in ["a", "e", "i", "o", "u"]:
#   print("The letter %s is a vowel." % letter)
# elif letter.upper() in ["A", "E", "I", "O", "U"]:
#   print("The letter %s is a vowel." % letter)
# else:
#   print("The letter %s is not a vowel." % letter)

"""
Scrivi un semplice programma che, data una lista di numeri, sommi tra loro tutti gli elementi.
Suggerimento: anche se esiste la funzione sum() per risolvere l'esercizio potresti usare il ciclo for.
"""
# numbers = [-1, 3, 15, 30, 45, 60, 2]
# sum = 0
# for i in range(len(numbers)):
#   sum = sum + numbers[i]
# print("The sum is %d." % sum)

"""
Scrivi un programma che a partire da un elemento e una lista di elementi dica in output se l'elemento passato sia presente o meno nella lista.
Qualora l'elemento sia presente nella lista, il programma dovrà comunicarci l'indice dell'elemento tramite il metodo index.
"""

el = "pino"

myList = ["paolo", "piero", "cariddi", "bicicletta", "piero", "pino", "paniere", "pino"]

# def checkIf(element, yourList):
#   if element in yourList:
#     index = yourList.index(element)
#     print("The element %s is inside the list and is in index %d" % (element, index))
#   else:
#     print("The element is not in the list.")

# checkIf(el, myList)

# OR -------

# found = False
# for item in myList:
#   if el == item:
#     found = True
#     break
    
# if found:
#   print("The element %s is inside your list and has index %d" % (el, myList.index(el)))
# else:
#   print("Your element is not inside the list.")

"""
Scrivi una semplice funzione che, data una lista di numeri, fornisca in output un istogramma basato su questi numeri, usando asterischi per disegnarlo.

Data ad esempio la lista [3, 7, 9, 5], la funzione dovrà produrre questa sequenza:

***

*******

*********

*****
"""
# myList = [3, 7, 9, 5]
# #i cicle all the numbers
# for number in myList:
#   #each cicle i create a void string
#   string = ""
#   for _ in range(number-1):
#     string = string + "*"
#   print("%s\n" % string)

"""
Scrivi una funzione che restituisca la lunghezza di una stringa o lista passata come parametro. In sostanza, seppur presente, provate a scrivere la nostra versione della funzione len!
"""

# def myLen(string):
#   myList = list(string)
#   counter = 0

#   for _ in myList:
#     counter+=1
  
#   return counter

# print(myLen("Capo"))

"""
Scrivi una funzione che data in ingresso una lista A contenente n parole, restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.

Questo esercizio può essere risolto anche usando una list comprehension.
"""
# myWords = ["pino", "giancarlo", "miriam", "giancarlo"]
# def fromListToIndexes(yourList):
#   myNumList = []
#   for word in yourList:
#     counter = 0
#     for letter in word:
#       counter+=1
#     myNumList.append(counter)
#   print(myNumList)

# OR

# def fromListToIndexes(yourList):
#   myNumList = [len(word) for word in yourList]
#   print(myNumList)

# fromListToIndexes(myWords)

"""
Scrivi una funzione che, data una stringa come parametro, restituisca un dizionario rappresentante la "frequenza di comparsa" di ciascun carattere componente la stringa.

Per fare un esempio, data una stringa "ababcc", otterremo in risultato {"a": 2, "b": 2, "c": 2}
"""

# def numOfCharSet(string):
#   mySet = {}
#   for letter in string:
#     if letter in mySet:
#       mySet[letter]+=1
#     else:
#       mySet[letter]=1
#   print(mySet)

# numOfCharSet("pinoni")

"""
Scrivi una funzione che, dato in ingresso un valore espresso in metri, mandi in print l'equivalente in miglia terrestri, iarde, piedi e pollici. Come risolverai questo esercizio?
"""

# def conversionMeters():
#   meters = input("Insert meters:\n")
#   milesPerM = 0.000621371
#   yardesPerM = 1.09361
#   feetsPerM = 3.28084
#   inchesPerMe = 39.3701

#   print("%.2f meters are %.5f in miles, %.2f in yardes, %.2f in feets and %.2f in inches" % (meters, meters*milesPerM, meters*yardesPerM, meters*feetsPerM, meters*inchesPerMe))

# conversionMeters()

"""
Scrivi una semplice funzione che converta un dato numero di giorni, ore e minuti, passati dall'utente tramite funzione input, in secondi.
"""

# def inSeconds():
#   myDict = {}
#   myDict["days"] = int(input("Insert days:\n"))
#   myDict["hours"] = int(input("Insert hours:\n"))
#   myDict["minutes"] = int(input("Insert minutes:\n"))

#   daysInS = myDict["days"] * 24 * 60 * 60
#   hoursInS = myDict["hours"] * 60 * 60
#   minutesInS = myDict["minutes"] * 60

#   sumSec = daysInS + hoursInS + minutesInS

#   print("The amount of seconds is: %d" % sumSec)


# inSeconds()

"""
Scrivi una funzione che, a scelta dell'utente, calcoli l'area di:

un cerchio
un quadrato
un rettangolo
un triangolo
Sentitevi liberi di estendere le potenzialità della funzione quanto meglio credete!
"""

"""
Un indirizzo MAC (Media Access Control address) è un indirizzo univoco associato dal produttore, a un chipset per comunicazioni wireless (es WiFi o Bluetooth), composto da 6 coppie di cifre esadecimali separate da due punti.

Un esempio di MAC è 02:FF:A5:F2:55:12.

Scrivi una funzione genera_mac() che generi degli indirizzi MAC pseudo casuali utilizzando il modulo random.
"""

# import random

# def getMAC():
#   listNum = []
#   letters = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
#   for _ in range(12):
#     ranNumber = random.randint(0,15)
    
#     myStr = ""
#     if ranNumber <= 9:
#       listNum.append(str(ranNumber))
#     else:
#       listNum.append(letters[ranNumber])
#     myFinalString = ""
#     for i in range(len(listNum)):
#       myFinalString += listNum[i]
#       if i%2 > 0 and i != 11:
#         myFinalString += ":"
#   print(myFinalString)

# getMAC()

"""
Scrivi una funzione che fornisca in output il nome del Sistema Operativo utilizzato con eventuali relative informazioni sulla release corrente.

Suggerimento: per risolvere questo esercizio potreste dover utilizzare una libreria! ;)
"""

# import platform

# myOs = platform.system()
# myOsRelease = platform.release()
# print("My Os is %s" %myOs)
# print("The current release is %s" %myOsRelease)

"""
Scrivi una funzione che, dato un carattere in ingresso, restituisca in output il codice ASCII associato al carattere passato.

Anche in questo caso, usare una libreria potrebbe facilitare la risoluzione dell'esercizio!
"""

# string = '"'
# print(ord(string))

"""
 Un numero perfetto è un numero naturale uguale alla somma dei suoi divisori positivi, escluso sé stesso. Scrivi una funzione che verifichi se un numero è perfetto oppure no.
"""

# def isPerfect():
#   number = input("Wich number you want to check if is number?\n")
#   dividersList = []
#   for i in range(1, number):
#     if number%i == 0 and i != number:
#       dividersList.append(i)
#   print(dividersList)
#   if sum(dividersList) == number:
#     print("Is perfect")
#   else:
#     print("It is not perfect.")

# isPerfect()

"""
Scrivi una funzione che aggiunga ad una lista 10 colori inseriti dall'utente. Il programma deve poi chiedere all'utente di inserire una lettera e mostrare in output solo i colori nella lista che iniziano con quella lettera.

Suggerimento: potresti usare la funzione range e il metodo startswith().
"""

# def colors():
#   myColors = []
#   for i in range(2):
#     color = input("Insert the color n°%d\n" % (i+1))
#     myColors.append(color.lower())
#   choosenLetter = input("Choose the start letter of the colors that you want.\n")
#   choosenColors = []
#   for color in myColors:
#     if color.startswith(choosenLetter):
#       choosenColors.append(color)
#       print(color)


# colors()

"""
Scrivi una funzione che prenda una serie di input dall'utente utilizzando un ciclo while e li stampi con la funzione print senza andare a capo. Il ciclo while si deve interrompere quando l'utente preme INVIO senza scrivere nulla.
"""

# def concatenateItems():
#   stop = False
#   itemsList = []
#   while stop == False:
#     item = input("Insert item:\n")
#     if item == "":
#       break
#     else:
#       itemsList.append(item)
#   myString = ""
#   for itm in itemsList:
#     myString += itm
#   print(myString)

# concatenateItems()

#  WE HAVE TO UNDERSTAND WHY THERE IS AN ERROR

"""
Scrivi una funzione che accetti una lista di dizionari rappresentante una scuola. Ogni dizionario rappresenta uno studente e contiene nome, cognome, classe e voti. La funzione deve stampare un elenco di tutti gli studenti e calcolare la media dei voti di ciascuno.
"""

# mySchool = [
#   {
#     "name": "Pino",
#     "surname": "Landi",
#     "class": "I A",
#     "grades": {
#       "math": 7,
#       "english": 9,
#       "history": 4,
#     }
#   },
#   {
#     "name": "Gianni",
#     "surname": "Spano",
#     "class": "II B",
#     "grades": {
#       "math": 3,
#       "english": 3,
#       "history": 6,
#     }
#   }
# ]

# def studentsAndAverage(school):
#   print("The students in the school are:")
#   for student in school:
#     grades = []
#     counter = 0
#     for key in student["grades"]:
#       grades.append(student["grades"][key])
#       counter+=1
#     average = sum(grades)/float(counter)
#     total_grades = sum(grades)
#     print("%s %s - grades average: %.2f" % (student["name"], student["surname"], average))
  
# studentsAndAverage(mySchool)

"""
Scrivi un programma che crei un file CSV per memorizzare in un dizionario i dati degli utenti registrati su un sito web. I dati richiesti per ogni utente sono: username, password, email e data di registrazione. Il programma deve permettere di salvare le informazioni nel file, leggere i dati e stamparli a schermo.
"""
# dataDic = [
#   {
#     "username" : "alemushy88",
#     "password": "ahdbc65432",
#     "email": "jhbu@jhv.it",
#     "reg_date": "14-12-1980"
#   },
#   {
#     "username" : "chicco88",
#     "password": "643jhvjg2",
#     "email": "vivamamma@ecco.it",
#     "reg_date": "07-03-1902"
#   },
#   {
#     "username" : "rapid88",
#     "password": "khjgk86",
#     "email": "pappa@gmail.it",
#     "reg_date": "12-06-2023"
#   },
# ]
# import csv
  
# myCSV = open("./data.csv", mode="w", newline="", encoding="ISO-8859-1")

# mywriter = csv.writer(myCSV)
  
# for user in dataDic:
#   myrow = []
#   for value in user:
#     myrow.append(user[value])
#   mywriter.writerow(myrow)
  
# myCSV.close()

# myCSV = open("./data.csv", mode="r", newline="", encoding="ISO-8859-1")

# myreader = csv.reader(myCSV, delimiter=",")

# data = [(line[0], line[1], line[2], line[3])for line in myreader]
# print(data)

"""
Scrivi una funzione che permetta di inserire una canzone e salvarla in un file di testo. Il programma deve chiedere all'utente di inserire il titolo e il testo della canzone, e poi salvare quest'ultimo in un file intitolato titolo_canzone.txt.

Suggerimento: dovrai utilizzare l'istruzione with.
"""

# def saveSong():
#   title = input("Insert song title:\n")
#   song = input("Insert the content of the song:\n")
#   filename = title + ".txt"
#   if title != "" and song != "":
#     file = open(filename, mode="w", encoding="ISO-8859-1")
#     file.write(song)
#   else:
#     print("You did not insert correct values.")

# saveSong()

"""
Scrivi una funzione che crei una tupla contenente i nomi dei pianeti del sistema solare, la loro tipologia (gassoso o roccioso) e il numero di satelliti naturali conosciuti. Il programma deve quindi stampare a schermo il contenuto della tupla e il numero totale di satelliti.
"""

# planets = [
#   {
#     "planet": "Mercury",
#     "type": "Rocky",
#     "satellites": 0
#   },
#   {
#     "planet": "Venus",
#     "type": "Rocky",
#     "satellites": 0
#   },
#   {
#     "planet": "Earth",
#     "type": "Rocky",
#     "satellites": 1
#   },
#   {
#     "planet": "Mars",
#     "type": "Rocky",
#     "satellites": 2
#   },
#   {
#     "planet": "Jupiter",
#     "type": "Gaseous",
#     "satellites": 95
#   },
#   {
#     "planet": "Saturn",
#     "type": "Gaseous",
#     "satellites": 83
#   },
#   {
#     "planet": "Uranus",
#     "type": "Gaseous",
#     "satellites": 27
#   },
#   {
#     "planet": "Neptune",
#     "type": "Gaseous",
#     "satellites": 14
#   },
# ]

# planetsTuple = tuple((planet["planet"], planet["type"], planet["satellites"])for planet in planets)

# print(planetsTuple)

"""
Scrivi una funzione che prenda come argomento un set di sport preferiti dall'utente e stampi un messaggio di testo che indica se si tratta di uno sport di squadra o individuale.

Suggerimento: per valutare la stringa inserita potrebbe essere utile utilizzare il metodo lower.
"""

def sport(favourite_sport):
  team_sports = {"soccer", "basketball", "volleyball", "ice hockey", "rugby", "football", "curling"}
  individual_sports = {"tennis", "golf", "boxing", "athletics", "surfing", "swimming", "cycling", "judo"}

  if favourite_sport.lower() in team_sports:
    print("It's a team sport!")
  elif favourite_sport.lower() in individual_sports:
    print("It's an individual sport!")
  else:
    print("Sport not recognized.")

sport("Cycling")

