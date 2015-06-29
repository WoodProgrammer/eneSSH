from Crypto.Cipher import AES
import base64


secret_key = 'key'.rjust(32) # create new & store somewhere safe

cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
def sifrele(x):
    x = x.rjust(32)
    encoded = base64.b64encode(cipher.encrypt(x))
    return encoded
def sifrecoz(x):

    decoded = cipher.decrypt(base64.b64decode(x))
    decoded = decoded.decode("utf-8")
    return decoded.strip()
