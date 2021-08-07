from math import pi, e 

def integral(f_string, bot, top):
    x = bot + 1e-10
    top_in = top - 1e-10
    delta_x = (top_in - x)/ 1e5
    
    res = 0
    
    while x < top_in:
        res += (eval(f_string)) * delta_x
        x += delta_x
    
    return res

bot = float(input('from = '))
top = float(input('to = '))
f_string = input('f = ')
print(integral(f_string, bot, top))
