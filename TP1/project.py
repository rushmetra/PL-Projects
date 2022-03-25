from ast import Str
from cgi import print_form
import re
import sys
import os
from unicodedata import numeric


# REGEX
cabecalho = r'([\wà-úÀ-Ú\/]+)({(\d),(\d)}|{(\d)})?((\:\:)([\wà-úÀ-Ú\/]+))?'
cab = re.compile(cabecalho)

corpo = r'([^,\n]*)'
ccorpo = re.compile(corpo)

def checkNumber (string):
    expNum = r"((\-|\+)?\d+(.\d+)?)"
    e = re.compile(expNum)
    t = re.findall(expNum,string)
    if t:
        return t[0][0]==string
    else:
        return False

def checkListNumber(lista):
    for i in lista:
        if not checkNumber(i):
            return False
    return True


def ler_ficheiro(file,saida):
    
    first_line = file.readline()
    lines = file.readlines()
    tokens = re.findall(cabecalho,first_line)
    
    saida.write("[\n")

    ## INDICE -> Avança quando acabar um tok
    for lin in lines:
        index = 0
        indice = 0
        toks = re.findall(corpo, lin)

        saida.write("\t{\n")
        
        for tok in tokens:
            if not tok[1]: # input nao é lista
                if checkNumber(toks[index]): # é numero
                    if indice==(len(tokens) - 1):
                        STR = "\t\t" + '"' + tok[0].rstrip('\n')+ '"' + ": " +  toks[index].rstrip('\n') + "\n"
                    else:
                        STR = "\t\t" + '"' + tok[0].rstrip('\n')+ '"' + ": " + toks[index].rstrip('\n') + ',' + "\n"
                else: # Nao é numero
                    if indice==(len(tokens) - 1):
                        STR = "\t\t" + '"' + tok[0].rstrip('\n')+ '"' + ": " + '"' + toks[index].rstrip('\n') + '"' + "\n"
                    else:
                        STR = "\t\t" + '"' + tok[0].rstrip('\n')+ '"' + ": " + '"' + toks[index].rstrip('\n') + '"' + ',' + "\n"
                index += 2
                saida.write(STR)
            else: # input é lista
                # verificar chavetas
                if not tok[4]:
                    # {a,b}
                    a = tok[2]
                    b = tok[3]
                    
                    n = index + (int(a)) + 2
                    maxIndex = index + (int(b)*2) - 1
                    i = index
                    lista = []

                    for index in range(i,n,2):
                        if toks[index]:
                            lista.append(toks[index])
                    
                    i = (n+1)

                    for index in range(i,maxIndex,2):
                        if toks[index]:
                            lista.append(toks[index])
                        else:
                            break
                    
                    if len(lista) != int(b):
                        index += int(b) - len(lista)
                    else:
                        index += 2
                    
                    
                else:
                    # {a}
                    a = tok[4]
                    n = index + (int(a))
                    i = index
                    lista = []
                    for index in range(i,n):
                        lista.append((toks[index]))
                        index += 1
                        
                numeric= checkListNumber(lista)
                # verificar se tem funcao
                if not tok[7]:
                    # nao tem funcao
                    if numeric:
                        if indice==(len(tokens) - 1):
                            STR = "\t\t" + '"' + tok[0].rstrip('\n')+ '"' + ": " + '['
                            s = ",".join(lista)
                            STR += s +']' + "\n"
                        else:
                            STR = "\t\t" + '"' + tok[0].rstrip('\n')+ '"' + ": " + '['
                            s = ",".join(lista)
                            STR += s +']'+ ',' + "\n"
                    else:
                        if indice==(len(tokens) - 1):
                            STR = "\t\t" + '"' + tok[0].rstrip('\n')+ '"' + ": " + '["'
                            s = '","'.join(lista)
                            STR += s +'"]' + "\n"
                        else:
                            STR = "\t\t" + '"' + tok[0].rstrip('\n')+ '"' + ": " + '["'
                            s = '","'.join(lista)
                            STR += s +'"]'+ ',' + "\n"
                    saida.write(STR)
                else:
                    #tem funcao
                    if numeric:
                        lista= list(map(float, lista))
                    func = tok[7] 
                    s=func + "(lista)"
                    result=eval(s)
                    if type(result) == int or type(result) == float:
                            result = '%g'%(result)
                            if indice==(len(tokens) - 1):
                                STR = "\t\t" + '"' + tok[0].rstrip('\n')+"_"+ func + '"' + ": " + str(result) + "\n"
                            else:
                                    STR = "\t\t" + '"' + tok[0].rstrip('\n')+"_"+ func + '"' + ": " + str(result) + ',' + "\n"
                    else:
                        if indice==(len(tokens) - 1):
                            STR = "\t\t" + '"' + tok[0].rstrip('\n')+"_"+ func + '"' + ": " +'"'+ str(result) + '"'+ "\n"
                        else:
                            STR = "\t\t" + '"' + tok[0].rstrip('\n')+"_"+ func + '"' + ": " +'"'+ str(result) + '"'+  ',' + "\n"
                    saida.write(STR)
            indice +=1            
        
        if lin==(lines[len(lines)-1]):
            saida.write("\t}\n")
        else:
            saida.write("\t},\n")
    
    saida.write("]")
    file.close()
    saida.close()


def main():
    print("Choose the file to process, press 'q' to quit.")
    for line in sys.stdin:
        line = line.rstrip('\n')
        if 'q' == line.rstrip():
            break
        filein = open(line,'r')
        if not filein:
            print("Invalid file, try again.")
            break
        else:
            filename = os.path.splitext(line)[0]
            filename += ".json"
            fileout = open(filename,'w')
            ler_ficheiro(filein,fileout)
            print("Done, see you later!")
            break

main()