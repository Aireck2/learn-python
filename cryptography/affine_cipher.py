"""
Affine cipher
Encryption formula:  c(x) = (A * x + B) mod 27
Decryption formula: d(x) = A_inv * (c(x) - B) mod 27

Where:
- x is the numeric position of the plaintext letter (0-26)
- A and B are the cipher keys (A must be coprime with 27 for decryption to work)
- A_inv is the modular multiplicative inverse of A mod 27
- 27 is the size of the alphabet (26 letters + Ñ)
"""

ALFABETO: str = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
MODULE: int = len(ALFABETO)

# Cipher key A: the multiplier in the affine function c(x) = Ax + B
# Must be coprime with MODULE (gcd(5, 27) = 1) for a valid inverse to exist
A: int = 5

# Cipher key B: the shift/additive constant in the affine function c(x) = Ax + B
B: int = 2

# Modular multiplicative inverse of A under modulus MODULE
# Satisfies: (A * A_INVERSO) mod MODULE = 1
# Here: (5 * 11) mod 27 = 55 mod 27 = 1 ✓
A_INVERSO: int = 11


def encrypt(text: str) -> str:
    """
    Encrypts plaintext.

    Applies the linear transformation c(x) = (A * x + B) mod 27 to each
    alphabetic character, where x is the letter's index in ALFABETO.

    Example:
        encrypt("USIL") -> encryption of each letter via c(x) = 6x + 2 (mod 27)
    """
    result = []
    text = text.upper()
    for letras in text:
        if letras in ALFABETO:
            x = ALFABETO.index(letras)
            # Apply encryption: c(x) = (A * x + B) mod MODULE
            cx = (A * x + B) % MODULE
            # Convert the encrypted numeric value back to a letter
            result.append(ALFABETO[cx])
        else:
            # Keep non-alphabetic characters unchanged
            result.append(letras)
    return "".join(result)


def decrypt(text: str) -> str:
    """
    Decrypts ciphertext encrypted .

    Reverses the encryption using the formula d(x) = A_inv * (c(x) - B) mod 27,
    where c(x) is the numeric index of the encrypted letter.

    Example:
        decrypt("encrypted") -> recovers original plaintext
    """
    result = []
    text = text.upper()
    for letras in text:
        if letras in ALFABETO:
            x = ALFABETO.index(letras)
            # Apply affine decryption: d(x) = A_inv * (x - B) mod MODULE
            dx = (A_INVERSO * (x - B)) % MODULE
            # Convert the decrypted numeric value back to a letter
            result.append(ALFABETO[dx])
        else:
            result.append(letras)
            # Keep non-alphabetic characters unchanged
    return "".join(result)


def main():
    """
    Entry point of the program.
    """

    message: str = "USIL"
    hidden_message: str = encrypt(message)
    decrypted_message: str = decrypt(hidden_message)

    print("CIFRADO AFIN")
    print("-------------")
    print("Original Message: ", message)
    print("Encripted Message: ", hidden_message)
    print("Decripted Message: ", decrypted_message)


if __name__ == "__main__":
    main()
