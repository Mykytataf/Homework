inp = 12
def time_of_year(num_of_month):
    Dict_of_year = {
        "Winter" : {12, 1, 2}, 
        "Spring" : {3, 4, 5},
        "Summer" : {6,7,8},
        "Autumn" : {9,10,11}
    }
    Winter = num_of_month == Dict_of_year["Winter"]
    Spring = num_of_month == Dict_of_year["Spring"]
    Summer = num_of_month == Dict_of_year["Summer"]
    Autumn = num_of_month == Dict_of_year["Autumn"] 
    if(Winter == True): 
        return("This month in Winter")
    elif(Spring == True):
        return("This month in Spring")
    elif(Summer == True):
        return("This month in Summer")
    elif(Autumn == True):
        return("This month in Autumn")
    else:
        return("Что-то тут не так")
Obj = time_of_year(inp)
print(Obj)