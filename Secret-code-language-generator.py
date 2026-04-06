import random
import string

def generate_random_chars(n=3):
    return ''.join(random.choice(string.ascii_letters) for _ in range(n))


def encode(word):
    if len(word) >= 3:
        transformed = word[1:] + word[0]
        prefix = generate_random_chars()
        suffix = generate_random_chars()
        return prefix + transformed + suffix
    else:
        return word[::-1]


def decode(word):
    if len(word) < 3:
        return word[::-1]
    else:
        stripped = word[3:-3]
        return stripped[-1] + stripped[:-1]


choice = input("Encode or Decode? (e/d): ").lower()
text = input("Enter your message: ")

words = text.split()
result = []

if choice == 'e':
    for w in words:
        result.append(encode(w))
    print("Encoded message:", " ".join(result))

elif choice == 'd':
    for w in words:
        result.append(decode(w))
    print("Decoded message:", " ".join(result))

else:
    print("Invalid choice!")