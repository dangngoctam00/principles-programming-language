//1813910
grammar BKIT;
@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
	tk = self.type
	result = super().emit()
	if tk == self.UNCLOSE_STRING:       
		raise UncloseString(result.text[1:])
	elif tk == self.ILLEGAL_ESCAPE:
		raise IllegalEscape(result.text[1:])
	elif tk == self.ERROR_CHAR:
		raise ErrorToken(result.text)
	elif tk == self.UNTERMINATED_COMMENT:
		raise UnterminatedComment()
	elif tk == self.STRING:
		result.text = self.text[1:-1]
		return result;
	else:
		return result;
}

options{
	language=Python3;
}

/*program  : VAR COLON ID SEMI EOF ;*/

program 			:glo_variable_dec* function_dec* EOF;
glo_variable_dec 	:VAR COLON list_var+ SEMICOLON; 

list_var 			:var_elem (COMMA var_elem)*;
var_elem			:var | var_init;
var_init			:variable_id EQUAL value;
var	 				:variable_id;
variable_id			:IDENTIFIER | (IDENTIFIER (LSB INTEGER RSB)+);
value 				:literal; //name ?

array 				:LCB array_elem+ RCB;
array_elem  		:array (COMMA array)? | value (COMMA value)*;
literal				:INTEGER | FLOAT | STRING | boolean | array;
unary_int			:(SUB_OP_INT | ADD_OP_INT)? INTEGER;
unary_float 		:(SUB_OP_FLOAT | ADD_OP_FLOAT)? FLOAT;
boolean 			:TRUE | FALSE;
function_dec 		:FUNCTION COLON IDENTIFIER parameter_dec? BODY COLON list_sta ENDBODY DOT;

list_sta 			:variable_dec* statement*;
parameter_dec 		:PARAMETER COLON list_param;
list_param 			:variable_id (COMMA variable_id)*;

statement 			:assignment_sta
					|if_sta
					|for_sta
					|while_sta
					|do_while_sta
					|break_sta
					|continue_sta
					|call_sta
					|return_sta
					;

if_sta 				:IF exp THEN list_sta (ELSEIF exp THEN list_sta)* (ELSE list_else_sta)? ENDIF DOT;
list_else_sta		:list_sta;
for_sta 			:FOR LP IDENTIFIER EQUAL exp COMMA exp COMMA exp RP DO list_sta ENDFOR DOT; // think assignment_exp
while_sta 	 		:WHILE exp DO list_sta ENDWHILE DOT;
do_while_sta 		:DO list_sta WHILE exp ENDDO DOT; // ? list_sta isn't used here
break_sta 			:BREAK SEMICOLON;
continue_sta 		:CONTINUE SEMICOLON;
call_sta 			:IDENTIFIER LP list_exp? RP SEMICOLON;
list_exp 			:exp (COMMA exp)*;
return_sta 			:RETURN exp? SEMICOLON;

variable_dec 		:VAR COLON list_var SEMICOLON;
// assignment_exp 		:left_operand EQUAL exp;
assignment_sta 		:left_operand EQUAL exp SEMICOLON;
left_operand 		:IDENTIFIER | (IDENTIFIER index_operators) | function_call index_operators;

exp 					:exp1 EQUAL_OP_INT exp1
						|exp1 NOT_EQUAL_OP_INT exp1		
						|exp1 LESS_OP_INT exp1		
						|exp1 GREATER_OP_INT exp1		
						|exp1 LESS_EQUAL_OP_INT exp1		
						|exp1 GREATER_EQUAL_OP_INT exp1		
						|exp1 NOT_EQUAL_OP_FLOAT exp1		
						|exp1 LESS_OP_FLOAT exp1		
						|exp1 GREATER_OP_FLOAT exp1		
						|exp1 LESS_EQUAL_OP_FLOAT exp1		
						|exp1 GREATER_EQUAL_OP_FLOAT exp1		
						|exp1
						;

exp1 					:exp1 AND_OP exp2
						|exp1 OR_OP exp2
						|exp2
						;

exp2 					:exp2 ADD_OP_INT exp3
						|exp2 SUB_OP_INT exp3
						|exp2 ADD_OP_FLOAT exp3
						|exp2 SUB_OP_FLOAT exp3
						|exp3
						;
exp3 					:exp3 MUL_OP_INT exp4
						|exp3 DIV_OP_INT exp4
						|exp3 MOD_OP_INT exp4
						|exp3 MUL_OP_FLOAT exp4
						|exp3 DIV_OP_FLOAT exp4
						|exp4
						;

exp4 					:NOT_OP exp4
						|exp5
						;

exp5 					:SUB_OP_INT exp5
						|SUB_OP_FLOAT exp5
						|exp6
						;

exp6 					:name_index_op index_operators
						|function_call
						;
name_index_op			:IDENTIFIER | function_call; //need to think carefully
// index_operators 		:(LSB exp RSB)+
index_operators			: LSB exp RSB | index_operators LSB exp RSB;

function_call 	 		:IDENTIFIER LP list_exp? RP  // exp7
						|exp8
						;
exp8 					:literal | IDENTIFIER | (LP exp RP);


// INT_OF_FLOAT							:'int_of_float';
// FLOAT_TO_INT 							:'float_to_int';
// INT_OF_STRING 							:'int_of_string';
// STRING_OF_INT 							:'string_of_int';
// FLOAT_OF_STRING 						:'float_of_string';
// STRING_OF_FLOAT 						:'string_of_float';
// BOOL_OF_STRING 							:'bool_of_string';
// STRING_OF_BOOL 							:'string_of_bool';
LP 										:'(';
RP 										:')';
LSB 									:'[';
RSB 									:']';
LCB 									:'{';
RCB 									:'}';
COLON 									:':';
SEMICOLON 								:';';
DOT 									:'.';
COMMA 									:',';
BODY  									:'Body';
BREAK 									:'Break';
CONTINUE 								:'Continue';
DO 										:'Do';
ELSE 	 								:'Else';
ELSEIF 									:'ElseIf';
ENDBODY  								:'EndBody';
ENDIF 									:'EndIf';
ENDFOR 									:'EndFor';
ENDWHILE 								:'EndWhile';
FOR 									:'For';
FUNCTION 								:'Function';
IF 										:'If';
PARAMETER 								:'Parameter';
RETURN 									:'Return';
THEN 									:'Then';
VAR 									:'Var';
WHILE 									:'While';
TRUE 	 								:'True';
FALSE 			  						:'False';
ENDDO 									:'EndDo';
EQUAL 									:'=';
ADD_OP_INT 								:'+';
SUB_OP_INT 								:'-';
MUL_OP_INT 								:'*';
DIV_OP_INT 								:'\\';
MOD_OP_INT 								:'%'; // \%
EQUAL_OP_INT 							:'==';
NOT_EQUAL_OP_INT 						:'!=';
GREATER_OP_INT 							:'>';
LESS_OP_INT 							:'<';
GREATER_EQUAL_OP_INT 					:'>=';
LESS_EQUAL_OP_INT 						:'<=';

ADD_OP_FLOAT 							:'+.';
SUB_OP_FLOAT 							:'-.';
MUL_OP_FLOAT 							:'*.';
DIV_OP_FLOAT 							:'\\.';
GREATER_OP_FLOAT 						:'>.';
LESS_OP_FLOAT 							:'<.';
GREATER_EQUAL_OP_FLOAT 					:'>=.';
LESS_EQUAL_OP_FLOAT 					:'<=.';
NOT_EQUAL_OP_FLOAT 						:'=/=';


NOT_OP 		 							:'!';
AND_OP 									:'&&';
OR_OP 									:'||';

fragment DIGIT    						:[0-9];
fragment NZERO_DIGIT 					:[1-9];
fragment LOWER_LETTER 					:[a-z];
fragment UPPER_LETTER 					:[A-Z];
fragment UNDERSCORE   					:'_';
fragment DECIMAL_PART 					:'.'[0-9]*;
fragment EXPONENT_PART 					:[eE] ('+' | '-')? [1-9]+;  //need think carefully
fragment ESCAPE_SEQUENCE         		:('\\' [nbfrt'\\]) | '\'"';
fragment ESCAPE_CHARACTER 				:[nbfrt'\\];
fragment ILLEGAL_ESCAPE_SQ 				:('\\' ~[nbfrt'\\]) | '\\' | ('\'' ~'"') ;


INTEGER 								:'0' | NZERO_DIGIT DIGIT* | (HEXA (NZERO_DIGIT | [A-F]) (DIGIT | [A-F])*) | (OCTAL (NZERO_DIGIT | [0-7]) (DIGIT | [0-7])*);//need to think carefully
FLOAT 									:('0' | NZERO_DIGIT DIGIT*) (DECIMAL_PART | EXPONENT_PART | DECIMAL_PART EXPONENT_PART); //need to think carefully

IDENTIFIER 	 							:LOWER_LETTER (UNDERSCORE | LOWER_LETTER | UPPER_LETTER | DIGIT)*;

// Literals
fragment HEXA 							:('0x' | '0X');
fragment OCTAL 							:('0o' | '0O');
fragment BOOLEAN 						: TRUE | FALSE;

STRING 									:'"'(~['"\\\n\r] | ESCAPE_SEQUENCE)*'"';
WS 										: [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
COMMENT 								:'**' .*? '**' -> skip;
ERROR_CHAR 								: .;
UNCLOSE_STRING 							:'"' (~(['"\\\r\n]) | ESCAPE_SEQUENCE)*;
ILLEGAL_ESCAPE 							:'"' (~['"\\\n] | ESCAPE_SEQUENCE)* ILLEGAL_ESCAPE_SQ;
UNTERMINATED_COMMENT 					:'**' (('*' ~'*')* | ~'*'*);