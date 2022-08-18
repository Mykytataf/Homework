


print('Введіть хвилини')
minutes = input()
minutes = int(minutes)
if(minutes > 60):
    while(minutes > 60):
        print('це надто багато, хвилин всього 60, спробуйте ще раз')
        minutes = input()
part_of_hour = minutes // 15
print(part_of_hour)