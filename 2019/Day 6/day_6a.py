def main():
    orbits = {}
    with open('input.txt', 'r') as f:
        program = f.read().splitlines()

    for row in program:
        outer_inner = row.split(')')
        orbits[outer_inner[1]] = [outer_inner[0]]

    counts = 0
    for orbit in orbits:
        all_orbits = get_all_orbits(orbits[orbit], orbits)
        counts += len(all_orbits) + 1

    print(counts)


def get_all_orbits(inner, orbits):
    if inner[0] in orbits:
        inner = inner + (get_all_orbits(orbits[inner[0]], orbits))
        return inner
    return []


main()
