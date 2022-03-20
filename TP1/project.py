import re
import sys


# REGEX
#cabecalho = r'([\wà-úÀ-Ú\/]+(\{\d(,\d)?\}(::[\wà-úÀ-Ú]+)?)?)'
cabecalho = r'([^,]+)'
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
    tokens = re.findall(cabecalho,first_line)
    lines = file.readlines()
    saida.write("[\n")
    index = 0

    for lin in lines:
        toks = re.findall(corpo, lin)

    ## o ultimo token tem um \n, por isso no ficheiro de output fica na linha de baixo "false"
    ## -> retirar o \n com alguma funcao pre-definida
    for tok in tokens:
        saida.write("\t{\n")
        for tok in tokens:
            str = "\t\t" + tok + ":" + toks[index] + "\n"
            index += 1
            saida.write(str)

        saida.write("\t}\n")

    saida.write("]")
    file.close()
    saida.close()

ler_ficheiro()
