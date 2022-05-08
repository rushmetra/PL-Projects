import ply.yacc as yacc
from lexer import tokens


def split(palavra):
    return [char for char in palavra]


def p_gramatica(p):
    "Gramatica : Lex Yacc "
    filename_out_parser = "out/parser.py"
    filename_out_lexer = "out/lexer.py"
    fileout1 = open(filename_out_parser,'w')
    fileout2 = open(filename_out_lexer,'w')
    fileout1.write(p[2])
    fileout2.write(p[1])
    fileout1.close()
    fileout2.close()

#LEX
def p_lex(p):
    "Lex : '%' '%' PAL ListNewLines List Defs Erro" 
    p[0] = "import ply.lex as lex\n\n" + p[5] + "\n"+ p[6] +"\n"+p[7]+"\n\n"+"lexer = lex.lex()"

def p_list(p):
    "List : Literals Ignore Tokens"
    p[0] = p[3] + "\n" +p[1] + "\n\n"+ p[2]+ "\n"

def p_literals(p):
    "Literals : '%' PAL '=' SIMB ListNewLines"
    p[0] = "literals = " + str(split(p[4][1:-1]))

def p_ignore(p):
    "Ignore : '%' PAL '=' SIMB ListNewLines"
    p[0] = "t_ignore =" + p[4] 

def p_tokens(p):
    "Tokens : '%' PAL '=' ListTokens ListNewLines"
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
    "Def : SIMB PAL '{' TOKEN ',' PAL Fim '}' ListNewLines "
    p[0] = "def t_" + p[4][1:-1] +"(t):\n\tr"+p[1] +"\n\tt.value = " + p[6]+p[7]+"\n\t"+p[2] + " t"

def p_erro (p):
    "Erro : '-' PAL SIMB ',' PAL Fim ')' ListNewLines"
    p[0] = "def t_error(t):\n\tprint(" + p[3]+")\n\t" + p[5]+p[6]


#YACC
def p_yacc (p):
    "Yacc : '%' '%' PAL ListNewLines Precedence Gramar Code "
    p[0] = "import ply.yacc as yacc\nfrom lexer import tokensp\n\n"+p[5]+"\n" + p[6] + p[7]

def p_precedence (p):
    "Precedence : '%' PAL '=' '[' ListNewLines ListPrecedence ']' ListNewLines"
    p[0] = p[2]+ p[3] + "(\n\t" +p[6]  + ")\n"

def p_listPrecedence_with_value(p):
    "ListPrecedence : PRECEDENCE ',' ListNewLines ListPrecedence"
    p[0] = p[1] + p[2] + "\n\t" + p[4]    

def p_listPrecedence_empty(p):
    "ListPrecedence : "
    p[0] = ""

def p_gramar_with_values(p):
    "Gramar : Productions Gramar"
    p[0] = p[1]+p[2]

def p_gramar_empty(p):
    "Gramar :"
    p[0] = ""

def p_productions_Productions(p):
    "Productions : PAL ':' Exp '{' Id  '}' ListNewLines"
    p[0] = "def p_"+p[1] +"(p):\n\t\"" + p[1]+ " : " + p[3] + "\"\n\t"  + p[5]  +"\n\n"

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
    "Id : Atr Math  ListAtr Fim"
    p[0] = p[1] + p[2] + p[3]+p[4]

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

def p_fim(p):
    "Fim : ')' "
    p[0] = p[1]

def p_fim_empty(p):
    "Fim : "
    p[0] = ""

def p_math_one (p):
    '''
    Math : '='
          | '+'
          | '-'
          | '*'
          | '/'
          | '_'
    '''
    p[0] = p[1]

def p_list_newlines_with_value(p):
    "ListNewLines : NEWLINE ListNewLines"

def p_list_newline_empty(p):
    "ListNewLines : "

def p_math_two (p):
    '''
    Math : '=' '+'
          | '=' '-'
    '''
    p[0] = p[1] + p[2]

def p_math_empty (p):
    "Math : "
    p[0] = ''

def p_code(p):
    "Code : '%' '%' ListNewLines ListDefsCode "
    p[0] = p[4]

def p_listdefscode_with_value(p):
    "ListDefsCode : DefsCode ListNewLines ListDefsCode"
    p[0] = p[1]+"\n"+p[3]

def p_listdefscode_empty(p):
    "ListDefsCode : "
    p[0] = ""

def p_DefsCode_Parser(p):
    "DefsCode : PAL '=' PAL ')' NEWLINE PAL SIMB ')' ListNewLines"
    p[0] = p[1] + p[2]+ "yacc." + p[3] + p[4] + "\n" + p[6] + p[7] + p[8] + '\n'

def p_DefsCode(p):
    "DefsCode : PAL PAL Fim ':' NEWLINE ListLinhaCode"
    p[0] = p[1]+" "+p[2]+p[3]+p[4]+p[6]+"\n"

def p_listLinhaCode_with_value(p): 
    "ListLinhaCode : LinhaCode ListLinhaCode "  
    p[0] = "\n" + p[1] + p[2]

def p_listLinhaCode_empty(p):
    "ListLinhaCode : "
    p[0] = ""

def p_linhaCode_with_value(p):
    "LinhaCode : ListElem ')' NEWLINE"
    p[0] = "\t" + p[1] + p[2]

def p_ListElem_with_value(p):
    "ListElem : Elem ListElem"
    p[0] = p[1] + p[2]

def p_ListElem_empty(p):
    "ListElem : "
    p[0] = "" 

def p_elem(p):
    '''
    Elem : PAL
          | TOKEN
          | SIMB
          | ':'
          | ','
          | '='
    '''
    p[0] = p[1] + " "


def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False

# Build the parser
parser = yacc.yacc()

# Read line from input and parse it

import sys

def main():
    print("Choose the file to process, press 'q' to quit.")
    for line in sys.stdin:
        filename_in = line.rstrip('\n')
        if 'q' == filename_in.rstrip():
            break
        filein = open(filename_in,'r')
        if not filein:
            print("Invalid file, try again.")
            break
        else:
            content = filein.read()
            parser.parse(content)
            filein.close()
            print("Done, see you later!")
            break

main()