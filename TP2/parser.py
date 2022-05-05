import ply.yacc as yacc
from lexer import tokens

def split(palavra):
    return [char for char in palavra]

def p_gramatica(p):
    "Gramatica : Lex Yacc"
    print(p[1])
    print(p[2])

#LEX
def p_lex(p):
    "Lex : '%' '%' PAL List Defs Erro" 
    p[0] = "import ply.lex as lex\n\n" + p[4] + "\n"+ p[5] +"\n"+p[6]+"\n\n"+"lexer = lex.lex()"

def p_list(p):
    "List : Literals Ignore Tokens"
    p[0] = p[3] + "\n" +p[1] + "\n\n"+ p[2]+ "\n"

def p_literals(p):
    "Literals : '%' PAL '=' SIMB"
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

def p_defs_with_value (p):
    "Defs : Def Defs"
    p[0] = p[1] + "\n\n" + p[2]

def p_defs_empty (p):
    "Defs : "
    p[0] = ""

def p_def (p):
    "Def : SIMB PAL '{' TOKEN ',' PAL '}'"
    p[0] = "def t_" + p[4][1:-1] +"(t):\n\tr"+p[1] +"\n\tt.value = " + p[6]+"\n\t"+p[2] + " t"

def p_erro (p):
    "Erro : '_' PAL SIMB ',' PAL"
    p[0] = "def t_error(t):\n\tprint(" + p[3]+")\n\t" + p[5][0:-1]


#YACC
def p_yacc (p):
    "Yacc : '%' '%' PAL Precedence Dicionary"
    p[0] = "import ply.yacc as yacc\nfrom lexer import tokensp\n\n"+p[4] + p[5]

def p_precedence (p):
    "Precedence : '%' PAL '=' '[' ListPrecedence ']' "
    p[0] = p[2]+ p[3] + "(\n\t" +p[5]  + ")\n"

def p_listPrecedence_with_value(p):
    "ListPrecedence : PRECEDENCE ',' ListPrecedence"
    p[0] = p[1] + p[2] + "\n\t" + p[3]    

def p_listPrecedence_empty(p):
    "ListPrecedence : "
    p[0] = ""

def p_dicionary_with_values(p):
    "Dicionary : Productions Dicionary"
    p[0] = p[1]+p[2]

def p_dicionary_empty(p):
    "Dicionary :"
    p[0] = ""

def p_productions_Productions(p):
    "Productions : PAL ':' Exp '{' Id  '}'" ##AQUI
    p[0] = "def p_"+p[1] +"(p):\n\t\"" + p[3] + "\"\n\t"  + p[5]  +"\n\n"

def p_exp_with_values(p):
    '''
    Exp : PAL Exp
        | TOKEN Exp
    '''
    p[0] = p[1] +" "+ p[2]

def p_exp_with_values_P(p):
    "Exp : '%' PAL Exp"
    p[0] = p[1] +" "+ p[2] +" "+ p[3]

def p_exp_empty(p):
    "Exp :"
    p[0] = ""

def p_id_at (p):
    "Id : Atr Math  ListAtr" #completar
    p[0] = p[1] + p[2] + p[3]

def p_atr (p):
    "Atr : PAL '[' Atr ']'"
    p[0] = p[1] + p[2] + p[3] + p[4]

def p_atr_empty (p):
    "Atr : PAL"
    p[0] = p[1]

def p_listAtr_with_values(p):
    "ListAtr : Atr Math ListAtr"
    p[0] = p[1] + p[2] + p[3]

def p_listAtr_empty(p):
    "ListAtr : "
    p[0] = ""

def p_math_one (p):
    '''
    Math : '='
          | '+'
          | '-'
          | '*'
          | '/'
    '''
    p[0] = p[1]

def p_math_two (p):
    '''
    Math : '=' '+'
          | '=' '-'
    '''
    p[0] = p[1] + p[2]

def p_math_empty (p):
    "Math : "
    p[0] = ''

    
def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False

# Build the parser
parser = yacc.yacc()

# Read line from input and parse it
f=open("teste",'r')
content = f.read()
result = parser.parse(content)