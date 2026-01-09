import argparse
import string
import secrets

def generate_password(length, use_upper, use_numbers, use_symbols):
    chars = string.ascii_lowercase

    if use_upper:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        raise ValueError("No character sets selected.")

    return ''.join(secrets.choice(chars) for _ in range(length))


def main():
    parser = argparse.ArgumentParser(
        description="Secure CLI Password Generator"
    )

    parser.add_argument("--length", type=int, default=12)
    parser.add_argument("--uppercase", action="store_true")
    parser.add_argument("--numbers", action="store_true")
    parser.add_argument("--symbols", action="store_true")

    args = parser.parse_args()

    try:
        password = generate_password(
            args.length,
            args.uppercase,
            args.numbers,
            args.symbols
        )
        print(password)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()

