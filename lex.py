import ply.lex as lex

reserved_words = {
	'while' : 'WHILE',
	'mixin' : 'MIXIN',
#	'import' : 'IMPORT',
	'include' : 'INCLUDE',
	'extend' : 'EXTEND'
}

tokens = [
	'IF',
	'ELIF',
	'ELSE',
	'ADD_OP',
	'MUL_OP',
	'NUMBER',
	'VARIABLE',
	'SELECTOR',
	'SEPARATOR',
	'STRING_VALUE',
	'SELECTOR_EXTEND',
 ] + list(reserved_words.values())

literals = '@();=:{},'

def t_IF(t):
	r'@if'
	return t

def t_ELIF(t):
	r'@else\ if'
	return t

def t_ELSE(t):
	r'@else'
	return t

def t_COMMENT(t):
	r'//.*'
	pass
	# No return value. Token discarded

def t_ADD_OP(t):
	r'[+-]'
	return t

def t_MUL_OP(t):
	r'[*/]'
	return t

def t_NUMBER(t): # 5px*10px
	r'\d+(\.\d+)?(px|%|em|rem|pt|cm|mm|in|pt|pc|ex|ch|vw|vh|vmin|vmax)?'
	return t

# t_FUNC_CSSV = ''

def t_VARIABLE(t):
	r'\$\w[A-Za-z-]+'
	if t.value in reserved_words:
		t.type = t.value.upper()
	return t

t_SEPARATOR = r'[>]'

def t_STRING_VALUE(t):
	r'[#\w-]+'
	if t.value in reserved_words:
		t.type = t.value.upper()
	return t

t_SELECTOR = r'\w[\w#.\-\[\]]*'

t_SELECTOR_EXTEND = r'\%\w[\w#.\-\[\]]*'

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
	print ("Illegal character '%s'" % repr(t.value[0]))
	t.lexer.skip(1)

lex.lex()

if __name__ == "__main__":
	import sys
	prog = open(sys.argv[1]).read()

	lex.input(prog)

	while 1:
		tok = lex.token()
		if not tok: break
		print ("line %d: %s(%s)" % (tok.lineno, tok.type, tok.value))
