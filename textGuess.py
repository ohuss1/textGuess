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
#print("nouns: "+nouns)
#to make sure eg:Apple and apple is counted as same
newnouns=nouns.lower()
#split newnouns string to list
nsplit=newnouns.split()
countword={}
for word in nsplit:
    countword.setdefault(word,0)
    countword[word]=countword[word]+1
print("topic is related to the follwing words")
for wordfreq in countword:
    if (int(countword.get(wordfreq))) > 1:
        highfreq = countword[wordfreq]
        
        print ((wordfreq)+": "+(str(highfreq)))



        
