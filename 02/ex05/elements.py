from elem import Elem, Text


class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('html', attr, content, 'double')


class Head(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('head', attr, content, 'double')


class Body(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('body', attr, content, 'double')


class Title(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('title', attr, content, 'double')


class Meta(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('meta', attr, content, 'simple')


class Img(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('img', attr, content, 'simple')


class Table(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('table', attr, content, 'double')


class Th(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('th', attr, content, 'double')


class Tr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('tr', attr, content, 'double')


class Td(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('td', attr, content, 'double')


class Ul(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('ul', attr, content, 'double')


class Ol(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('ol', attr, content, 'double')


class Li(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('li', attr, content, 'double')


class H1(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('h1', attr, content, 'double')


class H2(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('h2', attr, content, 'double')


class P(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('p', attr, content, 'double')


class Div(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('div', attr, content, 'double')


class Span(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('span', attr, content, 'double')


class Hr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('hr', attr, content, 'simple')


class Br(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('br', attr, content, 'simple')


def test():
    print('from subject:\n', Html([Head(), Body()]), '\n')

    print('from ex04:\n', Html([Head(Title(Text('Hello ground!'))), Body([H1(Text('Oh no, not again!')),
                                                          Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})])]), '\n')

    print('html:\n', Html(attr={'lang': 'en'}), '\n')
    print('head, title, meta:\n', Head([Title(Text('bbbbb')), Meta(attr={'charset': 'UTF-8'})]), '\n')
    print('body, p:\n', Body([P(Text('Some text')), P(Text('Another text'))]), '\n')
    print('img:\n', Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'}), '\n')
    print('h1:\n', H1(Text('header 1')), '\n')
    print('h2:\n', H2(Text('header 2')), '\n')
    print('div, table, th, td, tr, ul, ol, li:\n', Div(Table([Th(Td(Ul([Li(Text('1')), Li(Text('2'))]))),
                                                              Tr(Td(Ol([Li(Text('1')), Li(Text('2'))])))])), '\n')
    print('span:\n', Span(Text('Some text')), '\n')
    print('hr:\n', Hr(), '\n')
    print('br:\n', Br(), '\n')


if __name__ == '__main__':
    test()
