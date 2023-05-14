def unify(x, y, theta):
    if theta is None:
        return None
    elif x == y:
        return theta
    elif isinstance(x, str) and x.startswith('?'):
        return unify_var(x, y, theta)
    elif isinstance(y, str) and y.startswith('?'):
        return unify_var(y, x, theta)
    elif isinstance(x, list) and isinstance(y, list):
        return unify(x[1:], y[1:], unify(x[0], y[0], theta))
    else:
        return None

def unify_var(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    else:
        theta[var] = x
        return theta

def main():
    facts = [
        ['likes', 'John', '?x'],
        ['food', 'Apple'],
        ['food', 'Vegetable'],
        ['eats', 'Anil', 'Peanuts']
    ]

    query = ['likes', 'John', 'Peanuts']

    theta = {}
    for fact in facts:
        result = unify(query, fact, theta)
        if result is not None:
            print("Unification succeeded!")
            print("Substitution:")
            for key, value in result.items():
                print(key + " = " + str(value))
            break
    else:
        print("Unification failed.")

if __name__ == '__main__':
    main()
