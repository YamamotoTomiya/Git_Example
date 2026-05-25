from decimal import Decimal, getcontext
import hashlib


DIGITS = 100
EXTRA_PRECISION = 10

getcontext().prec = DIGITS + EXTRA_PRECISION


def arctan_inverse(x: int) -> Decimal:
    x = Decimal(x)
    term = Decimal(1) / x
    result = term

    n = 1
    sign = -1

    while True:
        term = term / (x * x)
        add = term / Decimal(2 * n + 1)

        if add == 0:
            break

        if sign > 0:
            result += add
        else:
            result -= add

        sign *= -1
        n += 1

    return result


def calculate_pi() -> Decimal:
    return 16 * arctan_inverse(5) - 4 * arctan_inverse(239)


def format_pi(pi: Decimal, digits: int) -> str:
    text = format(pi, "f")
    integer_part, decimal_part = text.split(".")
    return integer_part + "." + decimal_part[:digits]


def main():
    pi_text = format_pi(calculate_pi(), DIGITS)

    digest = hashlib.sha256(pi_text.encode("utf-8")).hexdigest()
  
    print("Algorithm:")
    print("Machin-like formula:")
    print("pi = 16 * arctan(1/5) - 4 * arctan(1/239)")
    print()
    print(f"Digits: {DIGITS}")
    print(pi_text)
    print()
    print("SHA-256:")
    print(digest)
    print("end")

if __name__ == "__main__":
    main()

