import ply.yacc as yacc
from lexer import tokens

def split(palavra):
    return [char for char in palavra]

def p_gramatica(p):
    "Gramatica : Lex"#add yacc
    print(p[1])

def p_lex(p):
    "Lex : '%' '%' PAL List Defs" 
    p[0] = "import ply.lex as lex\n\n" + p[4] + "\n"+ p[5] +"lexer = lex.lex()"

def p_list(p):
    "List : Literals Ignore Tokens"
    p[0] = p[3] + "\n" +p[1] + "\n\n"+ p[2]+ "\n"

def p_literals(p):
    "Literals : '%' PAL '=' SIMB"#alterar
    p[0] = "literals = " + str(split(p[4][1:-1]))

def p_ignore(p):
    "Ignore : '%' PAL '=' SIMB"
    p[0] = "t_ignore =" + p[4] 

def p_tokens(p):
    "Tokens : '%' PAL '=' ListTokens"
    p[0] = "tokens = [" + p[4] +"]"

def p_listtokens_with_value(p):
    "ListTokens : '[' TOKEN ListTokens ']'"
    p[0] = p[2] +p[3]

def p_listtokens_one(p):
    "ListTokens : ',' TOKEN"
    p[0] = p[1]+ p[2]

def p_listtokens_empty(p):
    "ListTokens : "

def p_defs_varias (p):
    "Defs : Def Defs"
    p[0] = p[1] + "\n\n" + p[2]

def p_defs_vazia (p):
    "Defs : "
    p[0] = ""

def p_def (p):
    "Def : SIMB PAL '{' TOKEN ',' PAL '}'"
    p[0] = "def t_" + p[4][1:-1] +"(t):\n\tr"+p[1] +"\n\tt.value = " + p[6]+"\n\t"+p[2] + " t"

def p_erro (p):
    "Erro : '.'"

def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False

# Build the parser
parser = yacc.yacc()

# Read line from input and parse it
f=open("teste",'r')
content = f.read()
result = parser.parse(content)