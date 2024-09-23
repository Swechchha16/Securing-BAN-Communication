from paillier import generate_paillier_keypair

def decrypt(private_key, public_key, ciphertext):
    n, g = public_key
    lam, mu = private_key
    n_sq = n * n
    def L(x):
        return (x - 1) // n
    x = pow(ciphertext, lam, n_sq)
    plaintext_int = (L(x) * mu) % n
    num_bytes = (plaintext_int.bit_length() + 7) // 8
    plaintext_bytes = plaintext_int.to_bytes(num_bytes, byteorder='big')
    return plaintext_bytes.decode(errors='ignore')

def decrypt_dataframe(encrypted_df, private_key, public_key):
    decrypted_data = {}
    for column in encrypted_df.columns:
        decrypted_data[column] = []
        for value in encrypted_df[column]:
            if pd.isna(value):
                decrypted_data[column].append(None)
            else:
                decrypted = decrypt(private_key, public_key, value)
                decrypted_data[column].append(decrypted)
    return decrypted_data
