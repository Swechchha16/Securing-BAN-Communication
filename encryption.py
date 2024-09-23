import pandas as pd
from paillier import generate_paillier_keypair
import random
import math

def encrypt(public_key, plaintext):
    n, g = public_key
    n_sq = n * n
    plaintext_bytes = plaintext.encode()
    plaintext_int = int.from_bytes(plaintext_bytes, byteorder='big')
    r = random.randint(1, n - 1)
    while math.gcd(r, n) != 1:
        r = random.randint(1, n - 1)
    c = (pow(g, plaintext_int, n_sq) * pow(r, n, n_sq)) % n_sq
    return c

def encrypt_dataframe(df, public_key):
    encrypted_data = {}
    for column in df.columns:
        encrypted_data[column] = []
        for value in df[column]:
            if pd.isna(value):
                encrypted_data[column].append(None)
            else:
                value_str = str(value)
                encrypted = encrypt(public_key, value_str)
                encrypted_data[column].append(encrypted)
    return encrypted_data
