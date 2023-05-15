import pytest

from project.lang.lang_utils import code2dot


def test_code2dot():
    hello_world = """digraph tree {
0 [label=prog];
0 -> 1;
1 [label=stmt];
1 -> 2;
2 [label=print];
2 -> 3;
3 [label=print];
2 -> 4;
4 [label=expr];
4 -> 5;
5 [label=val];
5 -> 6;
6 [label="Hello,  World!"];
0 -> 7;
7 [label=";"];
0 -> 8;
8 [label=<EOF>];
}
"""

    assert code2dot('print "Hello,  World!";') == hello_world
