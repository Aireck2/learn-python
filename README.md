# Learn Python

University workspace for learning Python, starting with classical cryptography.

Implements ciphers from scratch with runnable examples: affine cipher, RSA, and modular inverses.

## Overview

This repo is a hands-on study notebook for uni classes. Each module is self-contained, heavily commented in Spanish/English, and exposes `encrypt()` / `decrypt()` plus a `main()` demo.

| Module | Description | Key formulas |
|---|---|---|
| `cryptography/affine_cipher.py` | Affine cipher over 27-letter Spanish alphabet (`ABCDEFGHIJKLMNÑOPQRSTUVWXYZ`) | `c(x) = (A·x + B) mod 27`, `d(x) = A_inv·(c-B) mod 27` |
| `cryptography/rsa_cipher.py` | Educational RSA (small primes `P=61`, `Q=53`) | `c = m^E mod N`, `m = c^D mod N` |
| `cryptography/mod_multiplicative_inverse.py` | Modular inverse helper via `pow(n, -1, mod)` | `(E·D) mod PHI = 1` |

> [!NOTE]
> RSA here uses tiny primes (`N=3233`) for learning only. Never use this for real data — use 2048+ bit keys from a vetted library.

## Getting started

### Prerequisites

- Python 3.14+
- `venv` (bundled with Python)
- Git

### Setup with venv

```bash
git clone <your-repo-url>
cd learn-python

# 1. Create environment
python3 -m venv .venv

# 2. Activate it
source .venv/bin/activate  # macOS / Linux
# .venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

> [!TIP]
> Deactivate anytime with `deactivate`. VS Code will auto-detect `.venv` as interpreter.

## Run the samples

Each cipher runs standalone:

```bash
# Affine cipher (CIFRADO AFIN)
python cryptography/affine_cipher.py

# RSA cipher (CIFRADO RSA)
python cryptography/rsa_cipher.py

# Modular inverse demo
python cryptography/mod_multiplicative_inverse.py
```

Example output:

```text
CIFRADO AFIN
-------------
Original Message:  USIL
Encripted Message:  ...
Decripted Message:  USIL
```

Quick use in your own code:

```python
from cryptography.affine_cipher import encrypt as affine_encrypt, decrypt as affine_decrypt
from cryptography.rsa_cipher import encrypt as rsa_encrypt, decrypt as rsa_decrypt

print(affine_encrypt("USIL"))
print(affine_decrypt(affine_encrypt("USIL")))

cipher = rsa_encrypt("USIL")  # -> list[int]
print(cipher)
print(rsa_decrypt(cipher))    # -> "USIL"
```

## Project structure

```text
learn-python/
├── cryptography/
│   ├── affine_cipher.py            # c(x) = (5x + 2) mod 27
│   ├── rsa_cipher.py               # P=61, Q=53, E=17, D=2753
│   └── mod_multiplicative_inverse.py
├── requirements.txt                # numpy, matplotlib
└── README.md
```

## Resources

- [Modular arithmetic — Khan Academy](https://www.khanacademy.org/computing/computer-science/cryptography)
- [Affine cipher — Wikipedia](https://en.wikipedia.org/wiki/Affine_cipher)
- [RSA — Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- [Python `pow` with modular inverse](https://docs.python.org/3/library/functions.html#pow)

## Troubleshooting

**`ModuleNotFoundError: numpy / matplotlib`**

You forgot to activate venv or install requirements:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

**`ValueError: base is not invertible for the given modulus`**

`A` must be coprime with the modulus. For mod 27, valid `A` values share no factor with 27 (e.g. 5, not 3 or 9).

> [!IMPORTANT]
> If `python` points to system Python instead of `.venv`, use `python3` explicitly or re-activate the environment.
