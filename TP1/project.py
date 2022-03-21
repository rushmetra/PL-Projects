import re
import sys


# REGEX
cabecalho = r'([\wà-úÀ-Ú\/]+)({(\d),(\d)}|{(\d)})?((\:\:)([\wà-úÀ-Ú\/]+))?'

#cabecalho = r'([^,]+)'
cab = re.compile(cabecalho)

corpo = r'([^,]+)'
ccorpo = re.compile(corpo)



def ler_ficheiro():
    file = open("myfile2.txt",'r')
    saida = open("output2.txt",'w')
    
    first_line = file.readline()
    lines = file.readlines()
    tokens = re.findall(cabecalho,first_line)
    
    saida.write("[\n")

    print(tokens)
    
    for lin in lines:
        index = 0
        toks = re.findall(corpo, lin)
        print(toks)
        saida.write("\t{\n")
        
        for tok in tokens:
            if not tok[1]: # input nao é lista
                if index==(len(tokens) - 1):
                    str = "\t\t" + '"' + tok[0].rstrip('\n')+ '"' + ": " + '"' + toks[index].rstrip('\n') + '"' + "\n"
                else:
                    str = "\t\t" + '"' + tok[0].rstrip('\n')+ '"' + ": " + '"' + toks[index].rstrip('\n') + '",' + "\n"
                index += 1
                saida.write(str)
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

                # verificar se tem funcao
                if not tok[7]:
                    # nao tem funcao
                    str = "\t\t" + '"' + tok[0].rstrip('\n')+ '"' + ": " + '['
                    s = ",".join(lista)
                    s= s[:-1]
                    str += s +']' + "\n"
                    saida.write(str)
                    #print(str)
                else:
                    #tem funcao
                    func = tok[7] ## sum
                    #globals()[func]()

        if lin==(lines[len(lines)-1]):
            saida.write("\t}\n")
        else:
            saida.write("\t},\n")
    
    saida.write("]")
    file.close()
    saida.close()

ler_ficheiro()
