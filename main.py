def main():
    print("Enter two symbol space separated:")
    inlet = input()

    # Разделение строки по пробелам
    inlet = inlet.split(' ')
    # Разворот массива
    inlet.reverse()

    print(f"{inlet[0]} {inlet[1]}")
    return 0


if __name__ == '__main__':
    main()


