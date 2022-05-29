from path import Path


def main():
    try:
        Path.makedirs('folder')
    except FileExistsError:
        pass
    Path.touch('folder/file')
    f = Path('folder/file')
    f.write_lines(['Hello', 'world!'])
    print(f.read_text())


if __name__ == '__main__':
    main()