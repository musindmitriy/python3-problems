

def is_prime(number):
    """Эту функцию можно сильно оптимизировать. Подумайте, как"""

    if number == 1:
        return False  # 1 - не простое число

    for possible_divisor in range(2, number):
        if number % possible_divisor == 0:
            return False

    return True
