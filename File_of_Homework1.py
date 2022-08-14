print('Скільки є кур?')
chikens = input()
chikens = int(chikens)
legs_of_chickens = chikens * 2
print('Скільки свиней?')
pigs = input()
pigs = int(pigs)
legs_of_pigs = pigs * 4
print('Скільки корів?')
cows = input()
cows = int(cows)
legs_of_cows = cows * 4
all_legs = legs_of_chickens + legs_of_pigs + legs_of_cows
all_legs = str(all_legs)
print('Всього ніг тварин на фермі ' + all_legs)