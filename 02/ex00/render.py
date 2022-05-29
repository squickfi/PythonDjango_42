import sys


def parse_settings():
    file = open('settings.py', 'r')
    values = {}
    for line in file.readlines():
        lines = line.split('=')
        values[lines[0].strip()] = lines[1].strip().strip('\"')
    file.close()
    return values


def check_args():
    if len(sys.argv) != 2:
        raise Exception('Wrong number of arguments!')
    if not sys.argv[1].endswith('.template'):
        raise Exception('Wrong extension! You need .template')


def read_template():
    check_args()
    file = open(sys.argv[1])
    template_str = file.read()
    file.close()
    return template_str


def write_cv():
    try:
        string = read_template()
        values = parse_settings()
        file = open('CV.html', 'w')
        file.write(string.format(**values))
        file.close()
    except Exception as e:
        print('Error:', e)


if __name__ == '__main__':
    write_cv()
