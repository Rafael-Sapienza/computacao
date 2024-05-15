def transformeEmMaiuscula(s):
    if s.isalpha():
        if s.isupper():
            return s
        else:
            asc = ord(s)
            asc -= 32
            s = chr(asc)
            return(s)
        
def transformeEmMinuscula(s):
    if s.isalpha():
        if s.islower():
            return s
        else:
            asc = ord(s)
            asc += 32
            s = chr(asc)
            return(s)    
        

def makeDancingSentence(string):
    novaString = ''
    possibilidadesDeFlag = ['maiuscula','minuscula']
    counter = 0
    flag = possibilidadesDeFlag[counter]
    for s in string:
        if s != ' ':
            if flag =='maiuscula':
                s = transformeEmMaiuscula(s)
                novaString += s
            else:
                s = transformeEmMinuscula(s)
                novaString += s
            counter += 1
            flag = possibilidadesDeFlag[counter%2]
        else:
            novaString += ' '
    print(novaString)


def main():
    while True:
        try:
            string = input()
            makeDancingSentence(string)
        except EOFError:
            break 

main()