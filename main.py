import random

def component_generator(lower, upper, function):
    if function == "addition":
        symbol = '+'
        num1 = random.randint(lower, upper)
        if num1 > 10:
            num2 = random.randint(lower, 10)
        else:
            num2 = random.randint(lower, upper)

        result = num1 + num2
    return([num1, num2, symbol, result])

def formatter(components):
    blank_position = random.randint(1,2)
    
    if blank_position == 1:
        return('____  {}  {:4}  =  {}'.format(components[2],
                                                   components[1],
                                                   components[3]))
    else:
        return('{:<4}  {}  ____  =  {}'.format(components[0],
                                                   components[2],
                                                   components[3]))


def writer(filename, equations):
    with open(filename, 'w') as file:
        for equation in equations:
            file.write('{}\n'.format(equation))


def main():
    equations = []
    for n in range(1, 76):
        components = component_generator(1, 19, 'addition')
        equations.append(formatter(components))
    print(equations)
    writer('problems.txt', equations)

if __name__ == "__main__":
    main()
