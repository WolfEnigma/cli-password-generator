from password_generator import generate_password
import string

def test_password_length():
    pw = generate_password(16)
    assert len(pw) == 16

def test_password_characters():
    pw = generate_password(20)
    allowed_chars = string.ascii_letters + string.digits + string.punctuation
    assert all(c in allowed_chars for c in pw)

def test_password_variation():
    pw1 = generate_password(12)
    pw2 = generate_password(12)
    assert pw1 != pw2  # passwords should differ
