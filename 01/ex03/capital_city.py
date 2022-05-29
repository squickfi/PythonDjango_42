import sys


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
        key = states.get(sys.argv[1])
        if not key:
            print("Unknown state")
            return
        print(capital_cities.get(key))


if __name__ == '__main__':
    find_capital_city()
