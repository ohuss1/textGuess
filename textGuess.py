#lets read stopwords that we will filter out from text article
f=open("minimal-stop.txt","r")
stopwords_list=[]
for line in f:
    stopwords_list.append(line)

def rowparser(row):
    row = row.replace('"', '').replace("\\n","").replace("\\N","").replace("'", '').replace("[","").replace("]","")
    return row
stopwords_list=rowparser(str(stopwords_list))
f.close()
#our article is called fish.txt
m = open("fish.txt","r")
fish=""
for line in m:
    fish=fish+(line)
#testing print(fish)
fishn=(str.replace(fish,",", " "))
fishn=(str.replace(fish,", ", " "))

fishn=(str.replace(fish,".", ""))
fishn=(str.replace(fishn,".\n", " "))
fishn=(str.replace(fishn,"-", " "))
fishn=(str.replace(fishn,",",""))
fishn = fishn.strip(',')
fishn = fishn.strip('.')
#print(fishn)
#now lets remove stopwords
nouns=fishn
#storing words without spaces in list
fishsplit=fishn.split()
for word in fishsplit:
    if word in stopwords_list:
        nouns=(str.replace(nouns,(" "+(word)+" ")," "))
print("nouns: "+nouns)
        
