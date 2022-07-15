y = 5

def set_x(z):
    x = z
    global y
    global a
    y = x
    a = 7
    
print("y before set_x:", y)    
    
set_x(10)    
print("y afetr set_x:", y)
print("a after set_x:", a)    