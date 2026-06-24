from hello import hello

def test_default():
    assert hello() == "Hello, world"

def test_arg():
    assert hello("Sajedeh") == "Hello, Sajedeh"