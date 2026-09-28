"""
RSA cipher
Encryption formula:  c = (m ** E) mod N
Decryption formula:  m = (c ** D) mod N

Where:
- m is the numeric value of the plaintext character (ord(char))
- c is the numeric value of the encrypted character
- P and Q are two prime numbers (private)
- N = P * Q is the modulus (public)
- PHI = (P - 1) * (Q - 1) is Euler's totient
- E is the public exponent (must be coprime with PHI)
- D is the private exponent, the modular multiplicative inverse of E mod PHI
- N must be greater than the max character code to encrypt (N = 3233 > 256)
"""

# Prime numbers (private keys)
# Small primes for educational purposes. In real RSA use 1024+ bit primes.
P: int = 61
Q: int = 53

# Modulus: N = P * Q, part of public and private keys
N: int = P * Q  # 3233

# Euler's totient: PHI = (P - 1) * (Q - 1)
PHI: int = (P - 1) * (Q - 1)  # 3120

# Public exponent E: must be coprime with PHI (gcd(17, 3120) = 1)
E: int = 17

# Private exponent D: modular multiplicative inverse of E mod PHI
# Satisfies: (E * D) mod PHI = 1
# Here: (17 * 2753) mod 3120 = 46801 mod 3120 = 1 ✓
D: int = pow(E, -1, PHI)  # 2753


def encrypt(text: str) -> list[int]:
    """
    Encrypts plaintext with the public key (E, N).

    Applies the transformation c = (m ** E) mod N to each character,
    where m = ord(char) is the character's Unicode code point.

    Example:
        encrypt("USIL") -> [2239, 2680, 1877, 2726]
    """
    result = []
    for char in text:
        m = ord(char)
        # RSA encryption: c = m^E mod N
        c = pow(m, E, N)
        # Ciphertext is numeric, so we store integers
        result.append(c)
    return result


def decrypt(cipher: list[int]) -> str:
    """
    Decrypts ciphertext encrypted with RSA.

    Reverses the encryption using the formula m = (c ** D) mod N,
    where c is each encrypted integer, then converts back with chr(m).

    Example:
        decrypt([2239, 2680, 1877, 2726]) -> "USIL"
    """
    result = []
    for c in cipher:
        # RSA decryption: m = c^D mod N
        m = pow(c, D, N)
        # Convert the decrypted numeric value back to a character
        result.append(chr(m))
    return "".join(result)


def main():
    """
    Entry point of the program.
    """

    message: str = "USIL"
    hidden_message: list[int] = encrypt(message)
    decrypted_message: str = decrypt(hidden_message)

    print("CIFRADO RSA")
    print("-------------")
    print("Original Message: ", message)
    print("Encripted Message: ", hidden_message)
    print("Decripted Message: ", decrypted_message)


if __name__ == "__main__":
    main()
