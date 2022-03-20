import re, sys


# cabecalho = r'((?=,)?[\wà-úÀ-Ú]*(\{\d(,\d)?\}(:{2}(\w+))?)*)' 
# cabecalho = r'[^,]+(:{2}(\w+))?(,*)?'   
# cabecalho = r'([\wà-úÀ-Ú]+(\{\d(,\d)?\}(::(^\wà-úÀ-Ú]+))?)?)' # esta separa a função

# Expressão regular para capturar o cabeçalho
cabecalho = r'([\wà-úÀ-Ú]+(\{\d(,\d)?\}(::[\wà-úÀ-Ú]+)?)?)'
cab = re.compile(cabecalho)

# Abertura do ficheiro
file = open("emd.csv")

# Lê a primeira linha do ficheiro (cabeçalho) e
# Itera o match da RE para o tokens
first_line = file.readline().rstrip()
tokens = cab.finditer(first_line)
# Imprime os grupos de tokens
for tok in tokens:
   print(tok.group(1))

# Expressão regular para capturar o resto das linhas do ficheiro .csv
corpo = r'[\wà-úÀ-Ú]+'
ccorpo = re.compile(corpo)



'''
lines = file.readlines()
for line in lines:
    teste = ccorpo.finditer(line)
    for tes in teste:
        print(tes.group(1))
'''

close("emd.csv")