import ply.lex as lex

tokens = ['PAL','TOKEN','SIMB','INIT']
literals = ['=','[',']',',']

t_PAL = r'\w+'
t_TOKEN = r'\'\w+\''
t_SIMB = r'\"[^\"]+\"'
t_INIT = r'%(%)?'
t_ignore = " \t\n"

def t_error(t):
    print('Caráter ilegal: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()