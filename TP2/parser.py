import ply.yacc as yacc
from lexer import tokens

def p_gramatica(p):
    "Gramatica : Lex"#add yacc

def p_lex(p):
    "Lex : INIT PAL List" 

def p_list(p):
    "List : Literals Ignore Tokens"
    print(p[2])
    print(p[3])

def p_literals(p):
    "Literals : INIT PAL '=' SIMB"#alterar

def p_ignore(p):
    "Ignore : INIT PAL '=' SIMB"
    p[0] = "t_ignore =" + p[4] 

def p_tokens(p):
    "Tokens : INIT PAL '=' ListTokens"
    p[0] = "tokens = [" + p[4] +"]"

def p_listtokens_with_value(p):
    "ListTokens : '[' TOKEN ListTokens ']'"
    p[0] = p[2] +p[3]

def p_listtokens_one(p):
    "ListTokens : ',' TOKEN"
    p[0] = p[1]+ p[2]

def p_listtokens_empty(p):
    "ListTokens : "

def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False

# Build the parser
parser = yacc.yacc()

# Read line from input and parse it
f=open("teste",'r')
content = f.read()
result = parser.parse(content)