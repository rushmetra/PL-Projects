import ply.yacc as yacc
from lexer import tokensp

precedence=(
	('left','+','-'),
	('left','*','/'),
	('right','UMINUS'),
	)

def p_stat(p):
	"stat : VAR '=' exp "
	ts[t[1]]=t[3]

def p_stat(p):
	"stat : exp "
	print(t[1])

def p_exp(p):
	"exp : exp '+' exp "
	t[0]=t[1]+t[3]

def p_exp(p):
	"exp : exp '-' exp "
	t[0]=t[1]-t[3]

def p_exp(p):
	"exp : exp '*' exp "
	t[0]=t[1]*t[3]

def p_exp(p):
	"exp : exp '/' exp "
	t[0]=t[1]/t[3]

def p_exp(p):
	"exp : '-' exp % prec UMINUS "
	t[0]=-t[2]

def p_exp(p):
	"exp : '(' exp ')' "
	t[0]=t[2]

def p_exp(p):
	"exp : NUMBER "
	t[0]=t[1]

def p_exp(p):
	"exp : VAR "
	t[0]=getval(t[1])

def p_error(t):
	print(f "Syntax error at ’{t.value}’, [{t.lexer.lineno}]" )

def getval(n):
	if n not in ts : print(f "Undefined name ’{n}’" )
	return ts.get(n , 0 )

y=yacc.yacc()
y.parse("3+4*7")

