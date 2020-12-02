import sys

def main():
    file_ = open(input("Filename: "), 'r')
    orbits = file_.readlines()
    orbits = [x.strip().split(")") for x in orbits]

    # print(orbits)

    orbit_map = {}
    for orbit in orbits:
        orbit_map[orbit[1]] = orbit[0]
    
    num_orbits = 0
    for orbit_start in orbit_map:
        while orbit_start != "COM":
            num_orbits = num_orbits + 1
            orbit_start = orbit_map[orbit_start]

    print(num_orbits)

main()