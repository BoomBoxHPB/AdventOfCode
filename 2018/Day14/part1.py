import sys

def main():
    # file = open(sys.argv[1], 'r')
    # lines = file.readlines()

    recipes = [3,7]
    elf1_idx = 0
    elf2_idx = 1

    end_after = 430971

    while len(recipes) < (end_after + 10):
        recipe_sum = recipes[elf1_idx] + recipes[elf2_idx]
        if recipe_sum >= 10:
            recipes.append(1)
            recipe_sum -= 10
        recipes.append(recipe_sum)

        elf1_idx += recipes[elf1_idx] + 1
        elf1_idx %= len(recipes)

        elf2_idx += recipes[elf2_idx] + 1
        elf2_idx %= len(recipes)

        # print(recipes)

    print(recipes[end_after:end_after+10])
main()