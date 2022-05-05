import ply.lex as lex

tokens = ['PAL','TOKEN','SIMB','PRECEDENCE']
literals = ['+','-','*','/','=','%','_','[',']',',','{','}','.',':','(',')']

t_ignore = " \t\n"
t_PAL = r"[A-Za-z\.\(\)0-9]+"
t_TOKEN = r"\'[^\']+\'"
t_SIMB = r"\"[^\"]+\""
t_PRECEDENCE = r"\((\'[^\']+\'\,)+(\'[^\']+\')+\)"


def t_error(t):
    print('Caráter ilegal: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()