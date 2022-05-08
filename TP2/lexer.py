import ply.lex as lex

tokens = ['PAL','TOKEN','SIMB','PRECEDENCE','NEWLINE']
literals = ['+','-','*','/','=','%','_','[',']',',','{','}','.',':','(',')']

t_ignore = " \t"
t_PAL = r"[A-Za-z\.\(\_0-9]+"
t_TOKEN = r"\'[^\']+\'"
t_SIMB = r"\"[^\"]+\""
t_PRECEDENCE = r"\((\'[^\']+\'\,)+(\'[^\']+\')+\)"
t_NEWLINE = r"\n"

def t_error(t):
    print('Caráter ilegal: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()