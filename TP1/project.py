from ast import Str
from cgi import print_form
import re
import sys
from unicodedata import numeric


# REGEX
cabecalho = r'([\wà-úÀ-Ú\/]+)({(\d),(\d)}|{(\d)})?((\:\:)([\wà-úÀ-Ú\/]+))?'
cab = re.compile(cabecalho)

corpo = r'([^,\n]+)'
ccorpo = re.compile(corpo)

def verific_is_Num (string):
    exp = r"(\d+(.\d+)?)"
    e = re.compile(exp)
    t = re.findall(exp,string)
    if t:
        return t[0][0]==string
    else:
        return False

def verific_list_is_Num(lista):
    for i in lista:
        if not verific_is_Num(i):
            return False
    return True


def ler_ficheiro():
    file = open("myfile2.txt",'r')
    saida = open("output2.txt",'w')
    
    first_line = file.readline()
    lines = file.readlines()
    tokens = re.findall(cabecalho,first_line)
    
    saida.write("[\n")

    
    for lin in lines:
        index = 0
        toks = re.findall(corpo, lin)

        saida.write("\t{\n")
        
        for tok in tokens:
            if not tok[1]: # input nao é lista
                if verific_is_Num(toks[index]):
                    if index==(len(tokens) - 1):
                        STR = "\t\t" + '"' + tok[0].rstrip('\n')+ '"' + ": " +  toks[index].rstrip('\n') + "\n"
                    else:
                        STR = "\t\t" + '"' + tok[0].rstrip('\n')+ '"' + ": " + toks[index].rstrip('\n') + ',' + "\n"
                else:
                    if index==(len(tokens) - 1):
                        STR = "\t\t" + '"' + tok[0].rstrip('\n')+ '"' + ": " + '"' + toks[index].rstrip('\n') + '"' + "\n"
                    else:
                        STR = "\t\t" + '"' + tok[0].rstrip('\n')+ '"' + ": " + '"' + toks[index].rstrip('\n') + '",' + "\n"
                index += 1
                saida.write(STR)
            else: # input é lista
                # verificar chavetas
                if not tok[4]:
                    # {a,b}
                    a = tok[2]
                    b = tok[3]

                else:
                    # {a}
                    a = tok[4]
                    n = index + (int(a))
                    i = index
                    lista = []
                    for index in range(i,n):
                        lista.append((toks[index]))
                        
                numeric= verific_list_is_Num(lista)
                # verificar se tem funcao
                if not tok[7]:
                    # nao tem funcao
                    if numeric:
                        STR = "\t\t" + '"' + tok[0].rstrip('\n')+ '"' + ": " + '['
                        s = ",".join(lista)
                        STR += s +']' + "\n"
                    else:
                        STR = "\t\t" + '"' + tok[0].rstrip('\n')+ '"' + ": " + '["'
                        s = '","'.join(lista)
                        STR += s +'"]' + "\n"
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
                            STR = "\t\t" + '"' + tok[0].rstrip('\n')+"_"+ func + '"' + ": " + str(result) + "\n"
                    else:
                        STR = "\t\t" + '"' + tok[0].rstrip('\n')+"_"+ func + '"' + ": " +'"'+ str(result) + '"'+ "\n"
                    saida.write(STR)
                    
        if lin==(lines[len(lines)-1]):
            saida.write("\t}\n")
        else:
            saida.write("\t},\n")
    
    saida.write("]")
    file.close()
    saida.close()

ler_ficheiro()
