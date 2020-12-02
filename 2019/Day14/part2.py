import sys
import math

class Formula:
    def __init__(self, ingredients, quantity):
        self.ingredients = {}
        ingredients = ingredients.split(', ')
        for entry in ingredients:
            split = entry.split(' ')
            type = split[1]
            self.ingredients[type] = int(split[0])
        self.quantity = int(quantity)

    def __repr__(self):
        return "{}, {}".format(self.quantity, self.ingredients)

def main():
    f = open(input("Filename: "), 'r')
    f = [l.strip().split(' => ') for l in f.readlines()]

    formulas = {}
    for form in f:
        output = form[1].split(' ')
        formulas[output[1]] = Formula(form[0], output[0])

    formulas['ORE'] = Formula('1 ORE', '1')

    maxOre = 1000000000000
    
    fuel = int(628597 * 1.80)
    while True:
        outputs = {'FUEL': fuel}
        extras = {}

        while len(outputs) > 1 or 'FUEL' in outputs:
            newOutputs = {}
            for out in outputs:
                # print(out)
                formula = formulas[out]
                # print(formula)
                numNeeded = outputs[out]
                try:
                    extrasAvailable = extras[out]
                    extrasUsed = min(extrasAvailable, numNeeded)
                    numNeeded -= extrasUsed
                    extras[out] -= extrasUsed
                except:
                    pass

                copiesNeeded = math.ceil(numNeeded / formula.quantity)
                try:
                    extras[out] += (formula.quantity * copiesNeeded) - numNeeded
                except:
                    extras[out] = (formula.quantity * copiesNeeded) - numNeeded

                for ingredient in formula.ingredients:
                    try:
                        newOutputs[ingredient] += formula.ingredients[ingredient] * copiesNeeded
                    except:
                        newOutputs[ingredient] = formula.ingredients[ingredient] * copiesNeeded
                
            outputs = newOutputs
            # print(outputs)

        # print(outputs)
        if outputs['ORE'] > maxOre:
            print(fuel - 1)
            return
        
        fuel += 1

main()