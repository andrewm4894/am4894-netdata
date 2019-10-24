from am4894netdata.dev import hello

def test_hello():
    res = hello('hello!')
    assert res=='hello!'