# Combinaisons de 3 chiffres

def three_numbers():
    combinations = []
    for x in range(10):
        for y in range(x, 10):
            for z in range(y, 10):
                combinations.append(f"{x}{y}{z}")

    combinations.remove(combinations[0])
    result = ", ".join(combinations)
    print(result)


three_numbers()
