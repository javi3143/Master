def multlists(x,y):
    final = []
    for i in x:
        for p in y:
            final.append((i,p))
    


m7 = [d for d in range(1,100,1) if d%7==0]
       

m6 = [d for d in range(1,100,1) if d%6==0]

m9= [d for d in range(1,100,1) if d%9==0]


final = []
for i in m7:
    if i in m6:
        final.append(i)


final2 = m7 + m9

roll = [1,2,3,4,5,6]
twodice = {r*s for r in roll for s in roll}
final = set([elem for elem in twodice if elem < 11])

roll = [1,2,3,4,5,6,7,8,9,10]
s = {x for x in range(1,100,1)}
twodice = {r*s for r in roll for s in roll}
final = set([elem for elem in s if elem not in twodice])

def nonproducts(n):
    roll = list(range(1,n**2+1))
    roll0 = list(range(1,n+1))
    twodice = {r*s for r in roll0 for s in roll0}
    final = set([elem for elem in roll if elem not in twodice])
    
def modules(n):
    
    moduledict = {'AC50001' : 'Introduction to Data Mining',
    'AC50002' : 'Programming Languages for Data Engineering',
    'AC51001' : 'Internet and Computer Systems',
    'AC51002' : 'Software Development',
    'AC51003' : 'Software Engineering',
    'AC51004' : 'Agile Engineering',
    'AC51005' : 'Technology Innovation Management',
    'AC51007' : 'Computer Vision',
    'AC51008' : 'Graphics',
    'AC51009' : 'Multimedia Audio',
    'AC51010' : 'Computing the User Experience',
    'AC51011' : 'Big Data Analysis',
    'AC52001' : 'Database Systems',
    'AC52002' : 'Advanced Programming Techniques',
    'AC52008' : 'Research Frontiers (Computing)',
    'AC52009' : 'Secure Internet Programming',
    'AC52012' : 'Research Methods',
    'AC52013' : 'Human Computer Interaction and Usability Engineering'
    }

    for i in moduledict:
        if float(i[3]) == n or float(i[3]) == 0:
            return (moduledict[i])

def strcount(strings):
    dic = {}
    for i in strings:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic

def strcount2(strings):
    dic = {key:strings.count(key) for key in strings}
    return dic

def version(strings):
    dic = {}
    lista = []
    for i in strings:
        if i not in lista:
            lista.append(i)
            dic[i] = 1
        else:
            x = dic[i]
            lista.append(i+"_"+str(x))
            dic[i] += 1 
            
    return lista

def int_to_roman (num):
    dict = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
        [ 100, 'C'], [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'],
        [  10, 'X'], [  9, 'IX'], [  5, 'V'], [  4, 'IV'],
        [   1, 'I']]
    roman = ''
    i = 0 #initiate i = 0
    while num > 0:
        while dict[i][0] > num: 
            i+=1 #increments i to largest value greater than current num
        roman += dict[i][1] #adds the roman numeral equivalent to string
        num -= dict[i][0] #decrements your num
    return roman

