grammar lang;

prog: (stmt ';')* EOF;

stmt: bind | print;

bind: var '=' expr
    | var '=' lambda;

lambda: '@' var '->' expr;

print: 'print' expr;

var: NAME;
val: INT
   | STRING
   | '{' expr (',' expr)* '}'   // множество
   | '(' expr ',' expr ')'      // пара
   | '{' INT ':' INT '}'
   ;

expr:
   '(' expr ')'
  | var                                 // переменные
  | val                                 // константы
  | 'set' expr 'as' 'starts' 'of' expr  // задать множество стартовых состояний
  | expr '^~' expr                      // задать множество стартовых состояний
  | 'set' expr 'as' 'finals' 'of' expr  // задать множество финальных состояний
  | expr '~^' expr                      // задать множество финальных состояний
  | 'add' expr 'to' expr 'starts'       // добавить состояния в множество стартовых
  | expr '+~' expr                      // добавить состояния в множество стартовых
  | 'add' expr 'to' expr 'finals'       // добавить состояния в множество финальных
  | expr '~+' expr                      // добавить состояния в множество финальных
  | expr '.starts'                      // получить множество стартовых состояний
  | expr '.finals'                      // получить множество финальных состояний
  | 'reachable' 'in' expr               // получить все пары достижимых вершин
  | '*~*' expr                          // получить все пары достижимых вершин
  | expr '.vertices'                    // получить все вершины
  | expr '.edges'                       // получить все рёбра
  | expr '.labels'                      // получить все метки
  | 'map' expr 'with' lambda            // классический map
  | lambda '@m>' expr                   // классический map
  | 'filter' expr 'with' lambda         // классический filter
  | expr '@f>' lambda                   // классический filter
  | 'load' STRING                       // загрузка графа
  | expr '&' expr                       // пересечение языков
  | expr '+' expr                       // конкатенация языков
  | expr '|' expr                       // объединение языков
  | expr '*'                            // замыкание языков (звезда Клини)
  | expr 'smb' expr                    // единичный переход
  | expr 'in' expr;


WS: [ \t\n\r]+ -> skip;
NAME: [a-zA-Z_][a-zA-Z0-9]*;
INT: ([0-9]+);
STRING: '"' (~["\\] | '\\' ["\\tvbn])* '"';
COMMENT: '#' ~( '\r' | '\n' )* -> skip;
