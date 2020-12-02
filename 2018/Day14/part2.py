import sys

def main():
    # file = open(sys.argv[1], 'r')
    # lines = file.readlines()

    recipes = [3,7]
    elf1_idx = 0
    elf2_idx = 1

    end_sequence = [4,3,0,9,7,1]
    # end_sequence = [5,9,4,1,4]

    last_x = 0
    while True:
        recipe_sum = recipes[elf1_idx] + recipes[elf2_idx]
        if recipe_sum >= 10:
            recipes.append(1)
            recipe_sum -= 10
        recipes.append(recipe_sum)

        elf1_idx += recipes[elf1_idx] + 1
        elf1_idx %= len(recipes)

        elf2_idx += recipes[elf2_idx] + 1
        elf2_idx %= len(recipes)

        for x in range(last_x,len(recipes)-len(end_sequence)):
            if end_sequence == recipes[x:x+len(end_sequence)]:
                print(x)
                return
            last_x = x
        # print(recipes)

main()