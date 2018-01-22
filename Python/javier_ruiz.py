# Author: Javier Ruiz

def Main():
    name = input("Enter name of the file: ")
    file = open(name)
    names = file.read().upper().replace("'", "")
    namesList = names.splitlines()
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
    # Removes symbols and makes sure words are separated by just one space (where appropriate)
    for i in range(len(namesList)):         
        for j in range(len(namesList[i])):
            if namesList[i][j] not in alphabet:
                namesList[i] = namesList[i].replace(namesList[i][j], " ")
        while "  " in namesList[i]:
            namesList[i] = namesList[i].replace("  ", " ")
    # Splits lists elements by words, generating a list of lists
    for i in range(len(namesList)):       
        namesList[i] = namesList[i].split()
    # Process names and creates output txt file
    return Output(file,Tuples(namesList))

# Calculates the specific value of a name's letters
def ValueLetter(namesList,i,p,q):        
    dictvalues = {'A': 20,'B': 8,'C': 8,'D': 9,'E': 25,'F': 7,'G': 9,'H': 7,'I': 20,'J': 3,'K': 6,'L': 10,'M': 8,
    'N': 10, 'O': 15,'P': 8,'Q': 1,'R': 10,'S': 10, 'T': 10, 'U': 15, 'V': 7, 'W': 7, 'X': 3, 'Y': 7, 'Z': 1}
    letter = namesList[i][p][q]
    value = dictvalues[letter]
    if q == 0:
        value = 0
    elif q == len(namesList[i][p])-1:
        if letter == "E":
            value = 15
        else:
            value = 2
    else:
        value += q
    return value

# Generates (letter,value) tuples per name and calls Abbreviations function  
def Tuples(namesList):
    abbrsTuplesList = []
    tuplesLetterValue = []
    for i in range(len(namesList)):             
        for p in range(len(namesList[i])):
            for q in range(len(namesList[i][p])):
                tuplesLetterValue.append((namesList[i][p][q],ValueLetter(namesList,i,p,q)))
        Abbreviations(abbrsTuplesList,tuplesLetterValue)
        tuplesLetterValue = []
    return RemoveDuplicates(abbrsTuplesList)

# Generates abbreviations and append them along their value to a list of tuples
def Abbreviations(abbrsTuplesList,tuplesLetterValue):     
    abbre = []
    for p in range(1, len(tuplesLetterValue)):
        for q in range(p+1, len(tuplesLetterValue)):
            ab = tuplesLetterValue[0][0]+tuplesLetterValue[p][0]+tuplesLetterValue[q][0]
            value = tuplesLetterValue[0][1]+tuplesLetterValue[p][1]+tuplesLetterValue[q][1]
            abbre.append((ab, value))
    return abbrsTuplesList.append(abbre)           

# Creates a list of dictionaries and removes duplicates, keeping the one with smaller value per name
def RemoveDuplicates(abbrsTuplesList):        
    abbrsDictsList = []   
    for i in range(len(abbrsTuplesList)): 
        tempdict = {}  
        for p in range(len(abbrsTuplesList[i])):
            try:
                tempdict[abbrsTuplesList[i][p][0]]
            except:
                tempdict[abbrsTuplesList[i][p][0]] = abbrsTuplesList[i][p][1]
            else:
                if tempdict[abbrsTuplesList[i][p][0]] > abbrsTuplesList[i][p][1]:
                    tempdict[abbrsTuplesList[i][p][0]] = abbrsTuplesList[i][p][1]
        abbrsDictsList.append(tempdict)
        tempdict = {}
    return CountAndDiscard(abbrsDictsList)
                
# Discards abbreviations that occur in multiple names
def CountAndDiscard(abbrsDictsList):        
    countsDict = {}
    for i in range(len(abbrsDictsList)):     
        for p in abbrsDictsList[i]:
            try:
                countsDict[p]
            except:
                countsDict[p] = 1
            else:
                countsDict[p] += 1
    finalAbbrsList = []
    for i in range(len(abbrsDictsList)):
        tempfilter = []
        for p in abbrsDictsList[i]:
            if countsDict[p] > 1:
                continue
            else:
                tempfilter.append(p)
        finalAbbrsList.append(tempfilter)
    return LowestScoreAbbr(abbrsDictsList,finalAbbrsList)
        
# Discards everything but the abbreviation(s) with the lowest score
def LowestScoreAbbr(abbrsDictsList,finalAbbrsList):
    result = []
    for i in range(len(finalAbbrsList)):     
        minscore = 100 # random initial value
        minscoreabbr = ""
        tempresult = []
        for p in range(len(finalAbbrsList[i])):
            score = abbrsDictsList[i][finalAbbrsList[i][p]]
            if len(finalAbbrsList[i]) == 1:
                minscoreabbr = finalAbbrsList[i][p]
                continue
            elif score < minscore:
                minscore = abbrsDictsList[i][finalAbbrsList[i][p]]
                minscoreabbr = finalAbbrsList[i][p]
            elif score == minscore:
                minscoreabbr += " "+finalAbbrsList[i][p]
            else:
                continue
        tempresult.append(minscoreabbr)
        result.append(tempresult)
    return result

# Generates output file    
def Output(file, result):
    file.seek(0)                        
    names = file.read().splitlines()
    output = open('names_abbrevs.txt', 'w')
    for x,y in zip(names, result):
        output.write(x + '\n')
        output.write(y[0] + '\n')
    return output.close()

Main()

