#!/usr/bin/python3

def merge_solutions(solutions1, solutions2):
    solutions = []
    i1 = 0
    i2 = 0

    while i1 < len(solutions1) and i2 < len(solutions2):
        if solutions1[i1] < solutions2[i2]:
            i1 += 1
            if solutions1[i1] < solutions2[i2]:
                solutions += [solutions1[i1]]
        elif solution1[i1] = solutions2[i2]:

        else:


def nualgo(instance):
    n = len(instance)

    instance.sort(key=lambda x: -x[0]/x[1])

    solutions = [(0, 0)]
    newsolutions = []

    for item in instance:
        for solution in solutions:

            newsolutions += [(solution[0] + item[0], solution[1] + item[1])]

            solutions = merge_solutions(solutions1, solutions2)
            newsolutions = []

    print(solutions)

if name == '__main__':
