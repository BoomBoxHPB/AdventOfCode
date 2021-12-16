def main():
    filename = input("Filename: ")
    file = open(filename, mode='r')

    links = [line.strip().split('-') for line in file.readlines()]
    link_dict = {}
    for link in links:
        first, second = link
        if first not in link_dict:
            link_dict[first] = []
        if second not in link_dict:
            link_dict[second] = []
        link_dict[first].append(second)
        link_dict[second].append(first)

    paths = []

    def navigate(path):
        if path[-1] == 'end':
            paths.append(path)
            return

        for link in link_dict[path[-1]]:
            if link[0].islower() and link in path:
                continue
            new_path = path[:]
            new_path.append(link)
            navigate(new_path)

    navigate(['start'])
    # print(paths)
    print(len(paths))

    paths = []
    def navigate_2(path, dupe_found):
        if path[-1] == 'end':
            paths.append(path)
            return

        for link in link_dict[path[-1]]:
            new_dupe_found = dupe_found
            if link == 'start':
                continue
            if link[0].islower() and link in path:
                if dupe_found:
                    continue
                new_dupe_found = True
            path.append(link)
            navigate_2(path, new_dupe_found)
            path.pop()

    navigate_2(['start'], False)
    print(len(paths))
    # for p in paths:
    #     print(','.join(p))

main()
