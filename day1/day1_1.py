
lines = []


def sumTo2020(lines):
    seen = set([])

    low = 0

    while low < len(lines):
        aux = int(lines[low])
        if 2020-aux in seen:
            return(aux * (2020-aux))
        else:
            seen.add(aux)
            low += 1

    return None


with open("./input.txt") as file:
    lines = [line.strip() for line in file]
print(f"Result Found: {sumTo2020(lines)}")
