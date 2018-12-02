#!/usr/bin/env python
# -*- coding: utf-8 -*-


import csv
import random

def help():
    print "\n"
    print "count(route, column, compare); \t \t \t \t print if compare in row[column]"
    print "filtro(route, column, criteria);  \t \t \t print if criteria in row[column]"
    print "values(route, column),  \t \t \t \t returns list with just that column"
    print "filtrar(routei, routeo, column, criteria),  \t \t if not criteria in row[column] => writerow"
    print "mayor(routei, routeo, column, criteria);  \t \t if row[column] >= criteria => writerow"
    print "menor(routei, routeo, column, criteria);  \t \t if row[column] <= criteria => writerow"
    print "contieneLista(routei, routeo, column, criteria);  \t criteria =[]; if any word from criteria in row[column] => writerow"
    print "minimizar (routei, routeo, column);  \t \t \t minimize row[column]"
    print "pasar(routei, routeo, cant, p);  \t \t \t pass random rows"
    print "partir(file, size);  \t \t \t \t \t split in as many output files as necessary with 'size' rows"
    print "\n"


def count(route, column, compare):
    f=open(route, "r")
    reader = csv.reader(f,delimiter=';')
    count=0
    for row in reader:
        if compare in row[column]:
            count = count + 1
    f.close()
    return count

def filtro(route, column, criteria):        #Printea valores que contengan la criteria
    f=open(route, "r")
    reader = csv.reader(f,delimiter=';')

    for row in reader:
        if criteria in row[column]:
            print row[column]
            print ""
    f.close()


def values(route, column):
    lista=[]
    f=open(route, "r")
    reader = csv.reader(f,delimiter=';')
    for row in reader:
        if row[column] not in lista: lista.append(row[column])
    lista.pop(0)
    f.close()
    return lista



def filtrar(routei, routeo, column, criteria):  #Bypassea tweets que cumplan la criteria

    f=open(routei, "r")
    out=open(routeo, "w+")
    reader = csv.reader(f,delimiter=';')
    writer = csv.writer(out,delimiter=';')
    count = 0

    writer.writerow(reader.next())
    for row in reader:
        try:
            if not criteria in row[column]:
                writer.writerow(row)
                count = count +1
        except: pass

    print str(count) + " Registros escritos"

    f.close()
    out.close()

def mayor(routei, routeo, column, criteria):  #Bypassea tweets que cumplan la criteria

    f=open(routei, "r")
    out=open(routeo, "w+")
    reader = csv.reader(f,delimiter=';')
    writer = csv.writer(out,delimiter=';')
    count = 0

    writer.writerow(reader.next())
    for row in reader:
        try:
            if float(row[column]) >= criteria:
                writer.writerow(row)
                count = count +1
        except: pass

    print str(count) + " Registros escritos"

    f.close()
    out.close()

def menor(routei, routeo, column, criteria):  #Bypassea tweets que cumplan la criteria

    f=open(routei, "r")
    out=open(routeo, "w+")
    reader = csv.reader(f,delimiter=';')
    writer = csv.writer(out,delimiter=';')
    count = 0

    writer.writerow(reader.next())
    for row in reader:
        try:
            if float(row[column]) <= criteria:
                writer.writerow(row)
                count = count +1
        except: pass

    print str(count) + " Registros escritos"

    f.close()
    out.close()


def contieneLista(routei, routeo, column, criteria):  #Bypassea tweets que cumplan la criteria

    f=open(routei, "r")
    out=open(routeo, "w+")
    reader = csv.reader(f,delimiter=';')
    writer = csv.writer(out,delimiter=';')
    count = 0

    writer.writerow(reader.next())
    for row in reader:
        try:
            if any(word in row[column] for word in criteria):
                writer.writerow(row)
                count = count +1
        except: pass

    print str(count) + " Registros escritos"

    f.close()
    out.close()

def clear(): print "\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n "



def vaciar(routei, routeo, column):
    f=open(routei, "r")
    out=open(routeo, "w+")
    reader = csv.reader(f,delimiter=';')
    writer = csv.writer(out,delimiter=';')
    count = 0

    writer.writerow(reader.next())
    for row in reader:
        try:
            if row[column] == "":
                writer.writerow(row)
                count = count +1
        except: pass

    print str(count) + " Registros escritos"

    f.close()
    out.close()

def minimizar (routei, routeo, column):
    f = open(routei, "r")
    out = open(routeo, "w+")
    reader = csv.reader(f, delimiter=';')
    writer = csv.writer(out, delimiter=';')
    for row in reader:
        try:
            row[column] = row[column].lower()
            writer.writerow(row)
        except: pass

    f.close()
    out.close()

def pasar(routei, routeo, cant, p):
    f = open(routei, "r")
    out = open(routeo, "w+")
    reader = csv.reader(f, delimiter=';')
    writer = csv.writer(out, delimiter=';')
    writer.writerow(reader.next())
    count=0


    for row in reader:
            if random.random() < p and count < cant:
                writer.writerow(row)
                count=count+1

    f.close()
    out.close()


def partir(file, size):
    i=0

    f = open (file, "r")
    reader = csv.reader(f, delimiter=";")
    header = reader.next()
    nameOfFile = "output"+str(i)+".csv"
    out = open(nameOfFile, "w+")
    writer = csv.writer(out, delimiter=";")
    writer.writerow(header)
    n=0

    for row in reader:
        n=n+1
        if n>size:
            out.close()
            i = i +1
            nameOfFile = "output"+str(i)+".csv"

            out = open(nameOfFile, "w+")
            writer = csv.writer(out, delimiter=";")
            writer.writerow(header)
            n=0
        writer.writerow(row)

    out.close()
    f.close()

def sentimentMean(file, column):
    f = open (file, "r")
    reader = csv.reader(f, delimiter=";")
    reader.next()
    sum = 0
    count = 0

    for line in reader:
    	sum = sum + float(line[column])
    	count = count + 1

    f.close()

    return (sum/count)

def GenerateName(filein, fileout):

    f = open (filein, "r")
    out = open(fileout, "w+")
    reader = csv.reader(f, delimiter=";")
    writer = csv.writer(out, delimiter=";")

    writer.writerow(reader.next())

    temp = []
    for row in reader:
        temp = row
        try: temp[0] = temp[9][20:(20+temp[9][20:].index("/"))]
        except: print temp
        writer.writerow(temp)

    f.close()
    out.close()

def TweetsAsText (filein):

    f = open (filein, "r")
    reader = csv.reader(f, delimiter=";")
    reader.next()

    text = ""
    for row in reader:
        text = text + " " + row[4]

    f.close()
    return text
