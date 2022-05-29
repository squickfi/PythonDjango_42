def my_var():
    var = 42
    print(var, "has a type", var.__class__)
    var = "42"
    print(var, "has a type", var.__class__)
    var = "quarante-deux"
    print(var, "has a type", var.__class__)
    var = 42.0
    print(var, "has a type", var.__class__)
    var = True
    print(var, "has a type", var.__class__)
    var = [42]
    print(var, "has a type", var.__class__)
    var = {42: 42}
    print(var, "has a type", var.__class__)
    var = (42,)
    print(var, "has a type", var.__class__)
    var = set()
    print(var, "has a type", var.__class__)


if __name__ == '__main__':
    my_var()
