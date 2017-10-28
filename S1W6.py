def codes(n):
    for i in n:
        x = ord(i)
        print (x)
    return

def firstlast():
    inp = input("Enter first string: ")
    while len(inp) != 0:
        if len(inp) == 1:
            print(inp)
            inp = input("Enter first string: ")
            continue
        length = len(inp)
        print(inp[0],"_"*(length-2),inp[-1])
        inp = input("Enter first string: ")
    
    return
        
             
def firstlastk (k):
    if k == 0:
        k = 1
    inp = input("Enter first string: ")
    while len(inp) != 0:
        number = k
        length = len(inp)
        if length > k*2:
            print(inp[:k],"_"*(length-2*k),inp[-k:])
            inp = input("Enter first string: ")
            
       
        else:
            print(inp)
            inp = input("Enter first string: ")
        
    return


def subseq2(s):
    string = ""
    for i in range(len(s)):
        if i < len(s)-1:
            k = 1    
            while i + k <=  len(s)-1:
                string += (s[i]+s[i+k])
                string += " "
                k += 1
            k =1
            
    print(string)
    return
""" wrong """        
def subseq3(s):
    string = ""
    for i in range(len(s)):
        if i < len(s)-2:
            k = 1
            q = 2
            while i + q <=  len(s)-1:
                string += (s[i]+s[i+k]+s[i+q])
                string += " "
                q += 1
            k =2
            q=3
        
            while i + k <= len(s)-2:
                
                string += (s[i]+s[i+k]+s[i+q])
                string += " "
                k += 1
            k =1
            q = 2
            
    print(string)
    return

def subsqn(string, k):
    result = ""
    reset = string
    number = k
    q=0
    if len(string) < k:
        result += " "+string
    for i in string:
        if len(string[q:]) >= number:
            result += " "+string[q:k]
            while len(string) > k:
                string = string[:k-1] + string[k:]
                result += " "+string[q:k]
           
        q += 1
        k += 1
        string = reset
    print(result[1:])

def dashify(string):
    final = ""
    for i in string:
        if string.index(i) < len(string)-1:
            final += i
            final += "_"
        else:
            final += i
    print(final)
    return

def avlen():
    inp = input("Enter a list of words: ")
    lista = inp.split()
    n = 0
    count = 0
    for i in lista:
        for e in i:
            count += 1
        n += 1
    print("Average word length: ",count/n)
    return


def guessstring(string):
    print("_ "*len(string))
    lettersguessed = list()
    count = 0
    index = ""
    while count < len(string):
        count = 0
        inp = input("Guess a letter: ")
        lettersguessed.append(inp)
        for letter in string:
            if letter in lettersguessed:
                index += letter
                count += 1
            else:
                index += " _ "
        print(index)
        index = ""
        
    return
    

    

        
    






















