import base64
import json

data = '{"showpassword":"no","bgcolor":"#ffffff"}'
cipher = "HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg="


def xor_strings(s1, s2):
    return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))


key = xor_strings(cipher, data)
print("Der Schlüssel ist:", key)
