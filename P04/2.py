alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(message, shift, left):
    print("\nEncrypted word: " + crypt(message, shift, left, decrypt=False))


def decrypt(message, shift, left):
    print("\nDecrypted word: " + crypt(message, shift, left, decrypt=True))


def crypt(message, shift, left=True, decrypt=False):
    message = message.lower()
    crypted = []

    if decrypt:
        left = not (left)

    for char in list(message):
        if char == ' ':
            crypted.append(char)
        else:
            # find char in alphabet
            try:
                index = alphabet.index(char)
            except ValueError:
                print("Character not allowed: " + char)

            new_pos = (index - shift if left else index + shift) % len(alphabet)

            if new_pos < 0:
                new_pos = len(alphabet) - new_pos

            crypted.append(alphabet[new_pos])

    return "".join(crypted)


message = input("Please type in your wished message: ")
shift = int(input("Please input your wished shift: "))
left = True if input('Want to shift to the left site (y/n)? ') == 'y' else False
crypt_method = True if input('Do you want to encrypt this message? (y/n)? ') == 'y' else False

if crypt_method:
    encrypt(message, shift, left)
else:
    decrypt(message, shift, left)
