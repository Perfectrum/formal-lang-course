grammar lang;

prog: (stmt ';')* EOF;

stmt: bind | print;

bind: var '=' expr
    | var '=' lambda;

lambda: '@' var '->' expr;

print: 'print' expr | expr;

var: NAME;
val: INT # Int
   | STRING # String
   | '{' expr (',' expr)* '}' # Set
   | '{' INT ':' INT '}' # Range
   ;

expr:
   '(' expr ')' # brackets
  | var # varExpr                                   // переменные
  | val # valExpr                                   // константы
  | 'set' expr 'as' 'starts' 'of' expr # setStarts  // задать множество стартовых состояний
  | 'set' expr 'as' 'finals' 'of' expr  # setFinals // задать множество финальных состояний
  | 'add' expr 'to' expr 'starts' # addStarts       // добавить состояния в множество стартовых
  | 'add' expr 'to' expr 'finals' # addFinal        // добавить состояния в множество финальных
  | expr '.starts' # starts                         // получить множество стартовых состояний
  | expr '.finals' # finals                         // получить множество финальных состояний
  | 'reachable' 'in' expr # reachable               // получить все пары достижимых вершин
  | expr '.vertices' # vertices                     // получить все вершины
  | expr '.edges' # edges                           // получить все рёбра
  | expr '.labels' # labels                         // получить все метки
  | 'map' expr 'with' lambda # map                  // классический map
  | 'filter' expr 'with' lambda # filter            // классический filter
  | 'load' STRING # load                            // загрузка графа
  | expr '&' expr # intersect                       // пересечение языков
  | expr '+' expr # concat                          // конкатенация языков
  | expr '|' expr # unify                           // объединение языков
  | expr '*' # kleeneStar                           // замыкание языков (звезда Клини)
  | expr 'smb' expr # smb                           // единичный переход
  | expr 'in' expr # in;

WS: [ \t\n\r]+ -> skip;
NAME: [a-zA-Z_][a-zA-Z0-9]*;
INT: ([0-9]+);
STRING: '"' (~["\\] | '\\' ["\\tvbn])* '"';
COMMENT: '#' ~( '\r' | '\n' )* -> skip;
