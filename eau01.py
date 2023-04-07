# Combinaisons de 2 nombres

def two_numbers():
    combinations = []
    for x in range(10):
        for y in range(x, 10):
            for a in range(y, 10):
                for b in range(a, 10):
                    combinations.append(f"{x}{y} {a}{b}")

    result = ", ".join(combinations)
    print(result)

two_numbers()