import pytest
import io

from project.lang.interpreter import Interpreter

interpreter = Interpreter()


def run(text: str):
    stream = io.StringIO()
    error = interpreter.interpret(text, stream)
    return stream.getvalue()


def test_in():
    assert run("print 1 in {1, 2, 3};") == "1\n"
    assert run("print {1} in {1, 2, 3};") == "1\n"
    assert run("print {1, 2} in {1, 2, 3};") == "1\n"

    assert run("print 42 in {1, 2, 3};") == "0\n"
    assert run("print {42} in {1, 2, 3};") == "0\n"
    assert run("print {1, 2, 3} in {42};") == "0\n"


def test_graph():
    assert run('wine = load "wine"; print wine.starts;') == "{}\n"
    assert run('wine = load "wine"; print wine.finals;') == "{}\n"

    assert (
        run(
            """
        wine = load "wine";
        wine = set {1, 2} as starts of
               set {3, 4} as finals of
               wine;
        print wine.starts;
        print wine.finals;
        print wine.labels;
    """
        )
        == "{1, 2}\n{3, 4}\n{}\n"
    )


def test_print():
    assert run("print 42;") == "42\n"
    assert run('print "Hello, World!";') == "Hello, World!\n"

    assert run("print {4, 2};") == "{2, 4}\n"
    assert (
        run('print {"Hello", "World"};')
        == str({"Hello", "World"}).replace("'", '"') + "\n"
    )

    assert run("print {2 : 4};") == "{2, 3}\n"


def test_bind():
    assert run("x = 42; print x;") == "42\n"
    assert run('hw = "Hello, World!"; print hw;') == "Hello, World!\n"


def test_map():
    assert (
        run(
            """
        print map {1, 2, 3, 100500} with @ x -> x in {1, 2, 3};
        """
        )
        == "[1, 1, 1, 0]\n"
    )


def test_filter():
    run(
        """
        wine = load "wine";
        print filter wine.vertices with @ x -> x in {1, 2, 3, 100500};
    """
    ) == "[1, 2, 3]\n"


def test_map_filter():
    run(
        """
        print map filter {1, 2, 3, 100500} with @x -> x in {1, 2, 3} with @x -> x in {1};
    """
    ) == "[1, 0, 0]\n"
