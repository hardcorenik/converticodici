import csv

def listaprova(isbn):
    miofile="/Users/nicolapietropaolo/Desktop/codici cideb copy/test/listalibri.csv"
    rowCnt=0
    mialista={}
    with open(miofile, 'rt') as f:
        reader = csv.reader(f, delimiter=',') #use pipe delimiter
        #for row in reader:
        #    if row[2]:
        #        mialista[row[2]]={"estero":row[1],"italia":row[0]}
        #    if row[3]:
        #        mialista[row[3]]={"estero":row[1],"italia":row[0]}
        #    if row[4]:
        #        mialista[row[4]]={"estero":row[1],"italia":row[0]}
        for row in reader:
            if row[0]:
                mialista[row[0]]={"ita":row[2],"vives":row[3],"ues":row[4]}
            if row[1]:
                mialista[row[1]]={"ita":row[2],"vives":row[3],"ues":row[4]}
    #for a in mialista.keys():
    #    if mialista[a]["ues"]:
    #        #sostituisci mialista[a] con mialista[a]["ues"]
    #        print(a,mialista[a]["ues"])
    #    if mialista[a]["vives"]:
    #        #sostituisci mialista[a] con mialista[a]["ues"]
    #        print(a,mialista[a]["vives"])
    #    if mialista[a]["ita"]:
    #        #sostituisci mialista[a] con mialista[a]["ues"]
    #        print(a,mialista[a]["ita"])
        risultato=[]
        for a in mialista.keys():
            if a==isbn:
                if mialista[a]["ues"]:
                    risultato.append(mialista[a]["ues"])
                if mialista[a]["vives"]:
                    risultato.append(mialista[a]["vives"])
                if mialista[a]["ita"]:
                    risultato.append(mialista[a]["ita"])
    return risultato

    #for a in mialista.keys():
    #    if a==isbn:
    #        if mialista[a]["ues"]:
    #            #sostituisci mialista[a] con mialista[a]["ues"]
    #            print(mialista[a]["ues"])
    #        if mialista[a]["vives"]:
    #            #sostituisci mialista[a] con mialista[a]["ues"]
    #            print(mialista[a]["vives"])
    #        if mialista[a]["ita"]:
    #            #sostituisci mialista[a] con mialista[a]["ues"]
    #            print(mialista[a]["ita"])

print(listaprova("9788853015143E"))
