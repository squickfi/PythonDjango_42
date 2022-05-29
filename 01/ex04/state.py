import sys


def find_value(dictionary, city):
    for key, value in dictionary.items():
        if value == city:
            return key
    return 'Unknown capital city'


def find_capital_city():
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    if len(sys.argv) == 2:
        value = find_value(capital_cities, sys.argv[1])
        print(find_value(states, value))


if __name__ == '__main__':
    find_capital_city()
