def my_numbers():
    file = open('numbers.txt', 'r')
    for line in file.read().strip().split(','):
        print(line)
    file.close()


if __name__ == '__main__':
    my_numbers()
