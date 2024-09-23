# Securing_WBAN_communication
## Overview  

This repository contains research and implementation related to securing wireless Body Area Sensor Networks (WBANs) communication using advanced encryption techniques. Specifically, we focus on employing a polymorphic encryption method to encrypt CSV file health data and using the Paillier key generation method to establish secure public and private keys for data encryption and decryption.  

## Table of Contents  

- [Introduction](#introduction)  
- [Key Features](#key-features)  
- [Implementation](#implementation)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Contributing](#contributing)  
- [Contact](#contact)  

## Introduction  

Wireless Body Area Networks (WBANs) are increasingly used in health monitoring applications to transmit sensitive health data. However, securing this communication is paramount to protect patient privacy and data integrity. This project explores the use of polymorphic encryption, which provides enhanced security by altering the encryption schema dynamically.  

The Paillier cryptosystem is utilized for key generation, enabling an efficient and secure way to manage public and private keys necessary for encryption and decryption processes.  

## Key Features  

- **Polymorphic Encryption**: Adapts encryption methods dynamically for enhanced security.  
- **Paillier Cryptosystem**: Utilizes a homomorphic encryption mechanism for secure key generation and data handling.  
- **CSV File Handling**: Specifically designed to handle CSV formats for health data seamlessly.  
- **Secure Communication**: Ensures secure transmission of sensitive health data in WBANs.  

## Implementation  

The implementation consists of the following components:  

1. **Key Generation**: Utilizes the Paillier method for generating public and private keys.  
2. **Data Encryption**: Applies polymorphic encryption to the health data stored in CSV files.  
3. **Data Decryption**: Provides functionality to decrypt the data securely using the generated keys.  

### Technologies Used  

- Python  
- Libraries: `numpy`, `pandas`, `cryptography`, etc.  

## Installation  

To work with this project, clone the repository and install the required dependencies. You can do this using the following command:  

```bash  
git clone https://github.com/109Shruti/Securing_WBAN_communication
cd Securing_WBAN_communication  
pip install -r requirements.txt`
```
## Folder Structure
1. **paillier.py: Manages key generation common to both encryption and decryption.**
2. **encryption.py: Handles encryption functionality.**
3. **decryption.py: Handles decryption functionality.**
4. **main.py: Coordinates everything, including reading the data, encrypting it, decrypting it, and saving the results.**

## Usage
Generate keys using the provided script:
```bash
python paillier.py
```
Encrypt health data stored in a CSV file:
```bash
python encryption.py input.csv encrypted_b.csv.csv
```
Decrypt the encrypted CSV file:
```bash
python decryption.py decrypted_b.csv decrypted.csv
```
Make sure to replace **input.csv** and **output.csv** with the appropriate file paths.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## Steps for Contributing  

1. **Fork the repository.**  
   
   Go to the repository page and click on the "Fork" button at the top right.  

2. **Create your feature branch.**  

   Open a terminal and run:  
   ```bash  
   git checkout -b feature/YourFeature

3. **Commit your changes**
   
    After making your changes, commit them with:
    ```bash
    git commit -m 'Add some feature'

4. **Push to the branch**

   Push your changes to your forked repository:
   ```bash
   git push origin feature/YourFeature

5. **Open a pull request**

   Go to the original repository where you want to merge your changes, and click on the "Pull       Requests" tab. Then click "New Pull Request" and select your branch.

## Contact
For questions or feedback, please reach out to:
@109Shruti, @Swechchha16

Email:
shrutidogra011@gmail.com ,
salonidixit2004@gmail.com

