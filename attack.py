import Rabin
import time


def optimized_attack(c, n, prefix="enc", length=9): # Меняем префикс и длину при необходимости
    alphabet = range(97, 123)  # a-z
    remaining_length = length - len(prefix)
    candidate = [0] * remaining_length

    def generate_word(pos):
        if pos == remaining_length:
            word = prefix + ''.join(chr(x) for x in candidate)
            m = Rabin.text_to_num(word)
            if pow(m, 2, n) == c:
                return word
            return None
        for char in alphabet:
            candidate[pos] = char
            result = generate_word(pos + 1)
            if result:
                return result
        return None

    start_time = time.time()
    result = generate_word(0)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Перебор занял: {elapsed_time:.2f} секунд")
    return result if result else "Not found"


def main():
    print("Запускаем Rabin.py для генерации c и n...")
    c, n = Rabin.main()  # Получаем c и n напрямую

    print(f"Атака на c = {c}, n = {n}")
    result = optimized_attack(c, n, prefix="enc", length=9)
    print("Найденное сообщение:", result)


if __name__ == "__main__":
    main()