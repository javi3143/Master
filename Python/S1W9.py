import re

def read():
    input = open("modules.txt")
    names = input.read()
    lines= names.splitlines()

    lista = []
    for i in lines:
        temp = []
        a = re.search(r'\sA{,1}?', i)
        index = a.start()
        temp.append(i[:index])
        temp.append(i[index+1:])
        lista.append(temp)

    dic = {}
    for i in lista:
        if i[0][3] not in ('0','1','2'):
            print("Incorrect format in code", i[0])
        elif len(i)!= 2:
            print ("Error in string ",i)
        else:
            dic[i[0]] = i[1]
    return dic


def func(oldfile, newfile):
    
    oldfile = oldfile.read()
    lines = oldfile.splitlines()

    lista = []
    while len(lines) > 0:
        try:
            temp = []
            temp.append(lines[1])
            temp.append(lines[0])
            lista.append(temp)
            lines = lines[2:]
        except:
            temp = []
            temp.append(lines[0])
            lista.append(temp)
            lines = []
            
    newfile = open("newfile.txt",'w')
    for x in lista:
        try:
            newfile.write(x[0]+ '\n')
            newfile.write(x[1]+ '\n')
        except:
            newfile.write(x[0])
            
    newfile.close()
    return newfile
