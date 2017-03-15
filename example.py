# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = [
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'ID',
   'ASSIGN',
   'SEMI',
   'ARROW',
   'LBRACKET',
   'RBRACKET',
   'COMMA',
   'LESS',
   'LESSEQUAL',
   'BIGGER',
   'BIGGEREQUAL'
]

reserved = {
   'array' : 'ARRAY',
   'by' : 'BY',
   'chars' : 'CHARS',
   'dcl' : 'DCL',
   'do' : 'DO',
   'down' : 'DOWN',
   'else' : 'ELSE',
   'elsif' : 'ELSIF',
   'end' : 'END',
   'exit' : 'EXIT',
   'fi' : 'FI',
   'for' : 'FOR',
   'if' : 'IF',
   'in' : 'IN',
   'loc' : 'LOC',
   'type' : 'TYPE',
   'od' : 'OD',
   'proc' : 'PROC',
   'ref' : 'REF',
   'result' : 'RESULT',
   'return' : 'RETURN',
   'returns' : 'RETURNS',
   'syn' : 'SYN',
   'then' : 'THEN',
   'to' : 'TO',
   'while' : 'WHILE',
   
   #Predefined Words
   
   'abs' : 'ABS',
   'asc' : 'ASC',
   'bool' : 'BOOL',
   'char' : 'CHAR',
   'false' : 'FALSE',
   'int' : 'INT',
   'length' : 'LENGTH',
   'lower' : 'LOWER',
   'null' : 'NULL',
   'num' : 'NUM',
   'print' : 'PRINT',
   'read' : 'READ',
   'true' : 'TRUE',
   'upper' : 'UPPER',
   'string' : 'STRING'
}

tokens = tokens + list( reserved.values() )

# Regular expression rules for simple tokens
t_PLUS    		= r'\+'
t_MINUS   		= r'-'
t_TIMES   		= r'\*'
t_DIVIDE  		= r'/'
t_LPAREN  		= r'\('
t_RPAREN  		= r'\)'
t_SEMI    		= r';'
t_ARROW   		= r'->'
t_ASSIGN   		= r'='
t_LBRACKET 		= r'\{'
t_RBRACKET 		= r'\}'
t_COMMA    		= r','
t_LESS     		= r'<'
t_LESSEQUAL		= r'<='
t_BIGGER     	= r'>'
t_BIGGEREQUAL  	= r'<='


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# STRING
def t_STRING(t):
	r'\".*\"'
	t.value = str(t.value)
	return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_ignore_comment(t):
    r'/\*(.|\n)*\*/'

def t_ignore_simple_comment(t):
	r'//.*'

def t_error_comment(t):
    r'/\*(.|\n)*'
    print("lineno: Unterminated comment")
    t.lexer.skip(1)
    
def t_error_string(t):
    r'\".*'
    print("lineno: Unterminated string")
    t.lexer.skip(1)


#def t_error_string(t):
#    r'/"(.|\n)*'
#    print("lineno: Unterminated comment")


# Build the lexer
lexer = lex.lex()


# Test it out
data = '''
/* aaa 

alkdjfadlks*/
//test
dcl m,n,s int;
i = "aaaaa"
read(m,n);
s = 0;
do while m <= n;
  s += m * n;
  print(m,s);
  m += 1;
od;
}
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
for tok in lexer:
    print(tok)
