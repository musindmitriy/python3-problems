
import itertools


def XOR_cipher(string, key):

    answer = []

    key = itertools.cycle(key)  # Повторяем ключ, чтобы зашифровать всю строку

    for s, k in zip(string, key):
        answer.append(chr(ord(s) ^ ord(k)))

    return ''.join(answer)

# Функция для расшифровки точно такая же
XOR_uncipher = XOR_cipher
