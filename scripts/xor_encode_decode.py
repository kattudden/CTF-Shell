import base64


def xor_encrypt_decrypt(input_string, key):
    # Konvertiere den Schlüssel in Bytes
    key_bytes = key.encode()
    key_length = len(key_bytes)

    # Erstelle eine Liste für das Ergebnis
    output = []

    # Iteriere über jeden Charakter im Eingabestring
    for i, char in enumerate(input_string):
        # XOR den Charakter mit dem entsprechenden Schlüsselbyte
        # Verwende modulo, um den Schlüssel zu wiederholen
        output_char = chr(ord(char) ^ key_bytes[i % key_length])
        output.append(output_char)

    # Verbinde die Liste in einen String
    return "".join(output)


def main():
    # Beispielverwendung
    original_text = base64.b64decode(
        "HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg="
    )
    key = "UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk"

    print(original_text)

    print(xor_encrypt_decrypt(original_text, key))


if __name__ == "__main__":
    main()
