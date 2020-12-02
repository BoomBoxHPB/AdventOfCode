import sys

def main():
    file_ = open(input("Filename: "), 'r')
    orbits = file_.readlines()
    orbits = [x.strip().split(")") for x in orbits]

    # print(orbits)

    orbit_map = {}
    for orbit in orbits:
        orbit_map[orbit[1]] = orbit[0]
    
    you_list = []
    orbit_start = "YOU"
    while orbit_start != "COM":
        you_list.append(orbit_map[orbit_start])
        orbit_start = orbit_map[orbit_start]

    san_list = []
    orbit_start = "SAN"
    while orbit_start != "COM":
        san_list.append(orbit_map[orbit_start])
        orbit_start = orbit_map[orbit_start]

    # print(you_list)
    # print(san_list)

    for step in you_list:
        if step in san_list:
            num_steps = you_list.index(step) + san_list.index(step)
            print(num_steps)
            return        

main()