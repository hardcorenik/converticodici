import csv
import sys
import string
import os

'''
Questo script prende in pasto:
A: un csv con una corrispondenza di idlibro / isbn
B: un file csv contenente una serie di codici univoci
alla fine restituisce X files (dipende da quanti idlibro sono presenti nel file corrispondenze)
contenenti i codici univoci e con il valore dell'isbn rimpiazzato dal valore dell'idlibro
'''

class Del:
	'''Rimuove i caratteri che non sono digits da una stringa di testo. Serve ad estrarre l'isbn dal nome file
	'''
	def __init__(self, keep=string.digits):
		self.comp = dict((ord(c),c) for c in keep)
	def __getitem__(self, k):
		return self.comp.get(k)

def Getidlibro(isbn):
	'''Prende un isbn come parametro e restituisce una lista contenente gli id corrispondenti
	'''
	miofile="/Users/nicolapietropaolo/Desktop/progetti/codici cideb/test/listalibri.csv"
	rowCnt=0
	listalibri={}
	with open(miofile, 'rt') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			if row[0]:
				listalibri[row[0]]={"ita":row[2],"vives":row[3],"ues":row[4]}
			if row[1]:
				listalibri[row[1]]={"ita":row[2],"vives":row[3],"ues":row[4]}
	risultato={}
	for a in listalibri.keys():
		if a==isbn:
			if listalibri[a]["ues"]:
				risultato["ues"]=listalibri[a]["ues"]
			if listalibri[a]["vives"]:
				risultato["vives"]=listalibri[a]["vives"]
			if listalibri[a]["ita"]:
				risultato["ita"]=listalibri[a]["ita"]
	return risultato

DD = Del()
parametro=sys.argv
miofile=parametro[1]
foutput='conv-'+parametro[1]
foutput=foutput.replace("Codici-", "")
resfoutput=foutput
print (foutput)
isbn=miofile.translate(DD) #rimuovo i caratteri non numerici dal nome del file così recupero l'isbn
print("isbn:",isbn)
rowCnt=0
mialista=[]
isbne=isbn+"E"
print (isbne)
with open(miofile, 'rt') as f:
	reader = csv.reader(f, delimiter=',')
	mialista = ['{1},{0},,5'.format(row[0], row[1]) for row in reader] #questa si chiama list comprhension
	#for row in reader:
	#	rowCnt+=1
		#if (rowCnt % 1000) == 0:
		#print '%s","%s'% (row[1],row[0])
	#	mialista.append(print ('{1},{0},,5'.format(row[0], row[1])))
	libridamodificare=Getidlibro(isbn)
	for key, value in libridamodificare.items():
		if os.path.exists(key):
		    print(key+" esiste")
		else:
		    os.mkdir(key)
		foutput="./"+key+"/"+value+"-"+str(foutput) #setto il nome del file che scriverò
		with open(foutput, 'w') as foutput:
			for row in mialista:
				if isbne in row:
					foutput.write((row.replace(isbn+"E", value))+'\n')
				else:
					foutput.write((row.replace(isbn, value))+'\n')
		print(foutput) #stampo i file che ho creato
		foutput=resfoutput
