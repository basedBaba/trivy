#!/usr/bin/env python3


import argparse
from cryptography.fernet import Fernet


def print_banner():
    print(r"""
                  ____              
      ___  ____  / __ \___  _____   
     / _ \/ __ \/ / / / _ \/ ___/   
    /  __/ / / / /_/ /  __/ /__     
    \___/_/ /_/_____/\___/\___/     
                                     
    """)


def get_args():
    parser = argparse.ArgumentParser(description="Encrypt/Decrypt files")

    parser.add_argument("command", help="encrypt/decrypt")
    parser.add_argument("file", help="file to be encrypted/decrypted")
    parser.add_argument("-k", "--key", help="secret key for decryption")

    args = parser.parse_args()

    if args.command == "decrypt" and not args.key:
        parser.error("enter the secret key for decryption")
        
    return args


def encrypt_file(file):
    key = Fernet.generate_key()

    with open(file, "rb") as read_file:
        content = read_file.read()
    
    encrypted_content = Fernet(key).encrypt(content)

    with open(file, "wb") as write_file:
        write_file.write(encrypted_content)

    key = key.decode("utf-8")
    
    print(f"The file {file} has been encrypted with the secret key {key}\nKeep it safe for decryption")


def decrypt_file(file, key):
    with open(file, "rb") as read_file:
        encrypted_content = read_file.read()
    
    decrypted_content = Fernet(key).decrypt(encrypted_content)

    with open(file, "wb") as write_file:
        write_file.write(decrypted_content)
    
    print(f"The file {file} has been decrypted")


def main():
    print_banner()

    args = get_args()

    if (args.command == "encrypt"):
        encrypt_file(args.file)

    if (args.command == "decrypt"):
        try:
            decrypt_file(args.file, args.key)
        except:
            print("Wrong secret key")


if __name__ == "__main__":
    main()