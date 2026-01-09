from password_generator import generate_password
import string

def test_password_length():
    pw = generate_password(16, True, True, True)
    assert len(pw) == 16

def test_password_characters():
    pw = generate_password(20, True, True, True)
    allowed = string.ascii_letters + string.digits + string.punctuation
    assert all(c in allowed for c in pw)

def test_cli_options():
    pw = generate_password(16, True, True, True)
    assert len(pw) == 16

