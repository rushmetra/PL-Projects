import ply.lex as lex

tokens = ['PAL','TOKEN','SIMB']
literals = ['=','%','[',']',',','{','}','.']

t_ignore = " \t\n"
t_PAL = r"[\w\.\(\)]+"
t_TOKEN = r"\'\w+\'"
t_SIMB = r"\"[^\"]+\""


def t_error(t):
    print('Caráter ilegal: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()