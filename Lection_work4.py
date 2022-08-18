inp = 3
def time_of_year(num_of_month):
    Dict_of_year = {
        "December" : 12,
        "January" : 1,
        "February" : 2,
        "March" : 3,
        "April" : 4,
        "May" : 5,
        "Juny" : 6,
        "July" : 7,
        "August" : 8,
        "September" : 9,
        "October" : 10,
        "November" : 11
    }
    
    Dict_of_year2 = {"month" : num_of_month}
    
    Winter = Dict_of_year2["month"] == Dict_of_year["December" or "January" or "February"]
    Spring = Dict_of_year2["month"] == Dict_of_year["March" or "April" or "May"]
    Summer = Dict_of_year2["month"] == Dict_of_year["Juny" or "July" or "August"]
    Autumn = Dict_of_year2["month"] == Dict_of_year["September" or "October" or "November"]
    if(Winter == True): 
        return("This month in Winter")
    elif(Spring == True):
        return("This month in Spring")
    elif(Summer == True):
        return("This month in Summer")
    elif(Autumn == True):
        return("This month in Autumn")
Obj = time_of_year(inp)
print(Obj)