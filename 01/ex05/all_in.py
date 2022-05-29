import sys


def find_state(dictionary, state):
    for key in dictionary:
        if key.lower() == state.lower():
            return dictionary[key]
    return None


def find_city(dictionary, city):
    for key, value in dictionary.items():
        if value.lower() == city.lower():
            return key
    return None


def all_in():

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
        args = sys.argv[1].split(',')
        for index in range(len(args)):
            args[index] = args[index].strip()
            if not args[index]:
                continue
            state = find_state(states, args[index])
            city = find_city(capital_cities, args[index])
            if state:
                print(capital_cities[state], 'is the capital of', find_city(states, state))
            elif city:
                print(capital_cities[city], 'is the capital of', find_city(states, city))
            else:
                print(args[index], 'is neither a capital city or a state')


if __name__ == '__main__':
    all_in()
