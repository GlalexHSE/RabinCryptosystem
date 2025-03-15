import random


def text_to_num(text: str):
    num = 0
    for char in text:
        num = num * 10000 + ord(char)
    return num


def num_to_text(num: int):
    text = ""
    while num > 0:
        char_code = num % 10000
        text = chr(char_code) + text
        num = num // 10000
    return text

#Тест Ферма
def is_prime(n, k = 10):
    if n < 2:
        return False
    if n == 2:  # 2 — наименьшее простое число
        return True
    for _ in range(10):  # 10 итераций для повышения точности
        a = random.randint(2, n - 1)
        if pow(a, n - 1, n) != 1:
            return False
    return True

def generate_large_prime():
    while True:
        num = random.randint(2**64, 2**128)
        if is_prime(num) and num % 4 == 3:
            return num

def key_generation():
    p = generate_large_prime()
    q = generate_large_prime()
    n = p * q
    key_pub = n
    key_priv = (p, q)
    return key_pub, key_priv


def encrypt(m: int, key_pub: int):
    n = key_pub
    c = pow(m, 2, n)
    return c


def decrypt(c: int, key_priv: tuple):
    p, q = key_priv
    n = p * q

    # Вычисляем кв.корни по модулю p и q:
    m_p = pow(c, (p + 1) // 4, p)
    m_q = pow(c, (q + 1) // 4, q)

    # Используем расширенный алгоритм Евклида для нахождения коэффициентов
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, x, y = extended_gcd(b % a, a)
            return g, y - (b // a) * x, x

    g, y_p, y_q = extended_gcd(p,q)

    # Используем Я и КТО:
    r_1 = (m_q * p * y_p + m_p * q * y_q) % n
    r_2 = n - r_1
    r_3 = (m_q * p * y_p - m_p * q * y_q) % n
    r_4 = n - r_3
    return r_1,r_2,r_3,r_4
def main():

    # Генерация ключей
    key_pub, key_priv = key_generation()
    print(f"Публичный ключ (n = p * q): {key_pub}")
    print(f"Приватный ключ (p, q):{key_priv}")

    # Ввод текста
    text = input("Введите текст: ")
    m = text_to_num(text)
    print(f"Числовое представление текста: {m}")

    #Зашифрование
    c = encrypt(m, key_pub)
    print(f"Зашифрованный текст(число): {c}")

    #Расшифрование
    r_1,r_2,r_3,r_4 = decrypt(c, key_priv)
    print(f"Возможные исходные тексты:\n 1:{num_to_text(r_1)} \n 2:{num_to_text(r_2)} \n 3:{num_to_text(r_3)} \n 4:{num_to_text(r_4)}")
while True:
    if __name__ == "__main__":
        main()