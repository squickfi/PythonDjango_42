class Intern:
    def __init__(self, name='My name? I’m nobody, an intern, I have no name.'):
        self.name = name

    def __str__(self):
        return self.name

    class Coffee:
        def __str__(self):
            return 'This is the worst coffee you ever tasted.'

    def work(self):
        raise Exception('I’m just an intern, I can’t do that...')

    def make_coffee(self):
        return Intern.Coffee()


def test_intern():
    intern1 = Intern()
    intern2 = Intern('Mark')
    print('intern1 name:', intern1.name)
    print('intern2 name:', intern2.name)
    print(intern2.name, 'made you coffee:', intern2.make_coffee())
    try:
        intern1.work()
    except Exception as e:
        print('I asked an intern to work but they said:', e)


if __name__ == '__main__':
    test_intern()
