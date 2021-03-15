from main import *


def test_greet1():
    assert (greet("Mr. Habib")) == "Hello, Mr. Habib"

def test_greet2():
    assert (greet("")) == "Hello, "

def test_greet3():
    assert (greet("Ryan")) == "Hello, Ryan"
