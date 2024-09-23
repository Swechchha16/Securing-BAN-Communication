from datetime import datetime
import pandas as pd
from paillier import generate_paillier_keypair
from encryption import encrypt_dataframe
from decryption import decrypt_dataframe

start_time = datetime.now()

# Define file path and load data
file_path = 'b.csv'

# Read a subset of the data for demonstration
df = pd.read_csv(file_path, nrows=10000)  # Adjust nrows for your dataset size

# Generate encryption keys
key_length = 512  # Adjust key length if needed
public_key, private_key = generate_paillier_keypair(key_length)

# Encrypt data
encrypted_data = encrypt_dataframe(df, public_key)

# Save encrypted data to CSV
encrypted_df = pd.DataFrame(encrypted_data)
encrypted_df.to_csv('encrypted_b.csv', index=False)

# Decrypt data (for verification, if needed)
encrypted_df = pd.read_csv('encrypted_b.csv')
decrypted_data = decrypt_dataframe(encrypted_df, private_key, public_key)

# Save decrypted data to CSV (if needed)
decrypted_df = pd.DataFrame(decrypted_data)
decrypted_df.to_csv('decrypted_b.csv', index=False)

print("Encryption and decryption complete.")
end_time = datetime.now()
print("Execution time:", end_time - start_time)
