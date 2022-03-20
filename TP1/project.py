import re
import sys


# REGEX
cabecalho = r'([\wà-úÀ-Ú\/]+(\{\d(,\d)?\}(::[\wà-úÀ-Ú]+)?)?)'
cab = re.compile(cabecalho)
#corpo = r'[\wà-úÀ-Ú-.@]+,?'
#corpo = r'[\wà-úÀ-Ú-.,@]+'


corpo = r'([^,]+)'
ccorpo = re.compile(corpo)


#3162,Cândido Faísca,Teatro,12,13,14,,
#7777,Cristiano Ronaldo,Desporto,17,12,20,11,12
#264,Marcelo Sousa,Ciência Política,18,19,19,20,



def ler_ficheiro():
    file = open("myfile.txt",'r')
    saida = open("output.txt",'w')
    first_line = file.readline()
    tokens = cab.finditer(first_line)
    lines = file.readlines()
    saida.write("[\n")
    index = 0

    for lin in lines:
        toks = re.findall(corpo, lin)

    for tok in tokens:
        saida.write("\t{\n")
        for tok in tokens:
            for i in tok.groups():
                if i != None:
                    str = "\t\t" + i + ":" + toks[index] + "\n"
                    index +=1
                    saida.write(str)
        saida.write("\t}\n")
    
        """
        for l in lins:
            saida.write("\t{\n")
            for i in l.groups():
                if i != None:
                    str = "\t\t" + i + "\n"
                    saida.write(str)
        saida.write("\t}\n")
        """

    saida.write("]")
    file.close()
    saida.close()
    """
    for tok in tokens:
        #print(tok.group(1))


    for line in lines:
        toks = ccorpo.finditer(line)
        #for t in toks:
        #    print(t.group(0))
    """

ler_ficheiro()
