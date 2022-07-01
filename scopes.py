y = 5

def set_x(y):
    print("inner y:", y)
    x = y
    y = x
    
set_x(10)    

print("Outer y:", y)    