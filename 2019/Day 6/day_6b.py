def main():
    orbits = {}
    with open('input.txt', 'r') as f:
        program = f.read().splitlines()

    for row in program:
        outer_inner = row.split(')')
        orbits[outer_inner[1]] = [outer_inner[0]]

    you_orbits = get_all_orbits(orbits['YOU'], orbits)
    santa_orbits = get_all_orbits(orbits['SAN'], orbits)

    meetup = ''
    stop = False
    for y in you_orbits:
        for s in santa_orbits:
            if y == s:
                meetup = y
                stop = True
                break
        if stop:
            break

    print(you_orbits.index(meetup) + santa_orbits.index(meetup))


def get_all_orbits(inner, orbits):
    if inner[0] in orbits:
        inner = inner + (get_all_orbits(orbits[inner[0]], orbits))
        return inner
    return []


main()
