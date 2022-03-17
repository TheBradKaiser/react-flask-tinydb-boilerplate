import os
import hashlib
def hashPassword(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    storage = salt+key
    return storage
def checkPassword(password,hashedpassword):
    salt=hashedpassword[:32]
    key = hashedpassword[32:]
    new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    if new_key ==key:
        return "correct password"
    else:
        return "incorrect password"
password = 'abc123'
hashy = hashPassword(password)
print(hashy)
check = checkPassword(password,hashy)
print(check)