from collections import Counter
import string


def main():
    # чтение первого файла
    file = open("text1.txt", 'r', encoding="utf8")
    text1 = file.read().lower().replace('\n', ' ')
    file.close()

    # чтение второго файла
    file = open("text2.txt", 'r', encoding="utf8")
    text2 = file.read().lower().replace('\n', ' ')
    file.close()

    count = 10  # количество выводимых значений

    # обработка первого текста
    # уберем знаки препинания
    text1 = text1.translate(str.maketrans('', '', string.punctuation))
    # делим текст по пробелу
    result_of_count1 = Counter(text1.split(' '))

    # обработка второго текста
    # уберем знаки препинания
    text2 = text2.translate(str.maketrans('', '', string.punctuation))
    # делим текст по пробелу
    result_of_count2 = Counter(text2.split(' '))

    # получение пересечения двух множеств(наборов)
    crossing = set(result_of_count1) & set(result_of_count2)

    # получение разницы двух множеств(наборов)
    uncrossing = set(result_of_count1) - set(result_of_count2)

    # вывод результата
    print(f"Топ {count} повторяющихся слов в тексте №1:")
    print("value\tkey")
    for key, value in result_of_count1.most_common(count):
        print(f"{value}\t:\t{key}")

    print("\nПовторяющиеся слова из двух тексов:")
    for word in crossing:
        print(word)

    print("\nНе повторяющиеся слова из двух тексов:")
    for word in uncrossing:
        print(word)

    return


if __name__ == '__main__':
    main()
