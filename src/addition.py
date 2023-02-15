# app.py
#this is my first github actions file

def add(a, c):
    return a + c

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
