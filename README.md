## What is this? ##
A python implementation of RSA-155, or 512 bit RSA.

## Non-cryptographically secure! ##
This is not a hardened implementation. Please don't use it for anything important. Also, RSA-155 has been insecure since like 1999, so just don't. Please.

## How to Run the Code ##

`pip install PyCryptodome` (if you don't already have it installed)
`python3 rsa.py`

If will generate `p` and `q` and print their value, along with those of `n` and `d`. It will then prompt you for the message to encrypt and print its encrypted value. Similarly, it will then prompt you for the message to decrypt and print its decrypted value.
