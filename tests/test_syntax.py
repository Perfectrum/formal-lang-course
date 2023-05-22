import pytest

from project.lang.lang_utils import check_syntax


def test_syntax_empty():
    assert check_syntax("\n")
    assert check_syntax("# comment")


def test_syntax_load():
    assert check_syntax('graph = load "graph";')


def test_syntax_bind():
    assert check_syntax('v = "Hello, World!";')
    assert check_syntax("v = 42;")
    assert check_syntax("v = (42);")
    assert check_syntax("v = {42};")
    assert check_syntax("v = (4, 2);")
    assert check_syntax("v = {1, 2, 3, 4, 5};")
    assert check_syntax("v = {1 : 100};")
    assert check_syntax("v = @ x -> x.labels;")


def test_syntax_print():
    assert check_syntax('print "Hello, World!";')
    assert check_syntax("print 42;")
    assert check_syntax("print (42);")
    assert check_syntax("print {42};")
    assert check_syntax("print (4, 2);")
    assert check_syntax("print {1, 2, 3, 4, 5};")
    assert check_syntax("print {1 : 100};")


def test_syntax_set_starts():
    assert check_syntax("set {1 : 42} as starts of g;")
    assert check_syntax("{1 : 42} ^~ g;")


def test_syntax_add_starts():
    assert check_syntax("add {1 : 42} to g starts;")
    assert check_syntax("{1 : 42} +~ g;")


def test_syntax_set_finals():
    assert check_syntax("set {1 : 42} as finals of g;")
    assert check_syntax("{1 : 42} ~^ g;")


def test_syntax_add_finals():
    assert check_syntax("add {1 : 42} to g finals;")
    assert check_syntax("{1 : 42} ~+ g;")


def test_syntax_reachable():
    assert check_syntax("reachable in g;")
    assert check_syntax("*~* g;")


def test_syntax_getters():
    assert check_syntax("g.starts;")
    assert check_syntax("g.finals;")
    assert check_syntax("g.vertices;")
    assert check_syntax("g.edges;")
    assert check_syntax("g.labels;")


def test_syntax_map():
    assert check_syntax("map g.vertices with @ v -> v in g.starts;")
    assert check_syntax("@ v -> v in g.starts @m> g.vertices;")


def test_syntax_filter():
    assert check_syntax("filter a.labels with @ label -> label in b.labels;")
    assert check_syntax("@ label -> label in b.labels @f> a.labels;")


def test_syntax_in():
    assert check_syntax("a in b;")
    assert check_syntax("a.labels in b.labels;")


def test_syntax_smb():
    assert check_syntax("a smb b;")


def test_syntax_langs_combinations():
    assert check_syntax("a & b;")
    assert check_syntax("a + b;")
    assert check_syntax("a | b;")


def test_syntax_clojure():
    assert check_syntax("a*;")
