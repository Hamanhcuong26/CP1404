import random

print("Welcome to the Gopher Population Simulator!")
print("Starting population: 1000")
print("Year 1")
print ("\n")
population = 1000
for year_num in range(2, 11):
    born_num = population * random.randint(10, 20) * 0.01
    die_num = population * random.randint(5, 25) * 0.01
    population = population + born_num - die_num
    print("{} gophers were born. {} died.".format(int(born_num), int(die_num)))
    print("Population: ", int(population))
    print("Year ", year_num)
    print ("\n")