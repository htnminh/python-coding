from termcolor import cprint

# every color
colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
for color in colors:
    if color != 'white':
        cprint(color, color, end = ' | ')
    else:
        cprint(color, color)

# examples of background colors
cprint('grey, on_yellow', 'grey', 'on_yellow', end = ' | ')
cprint('blue, on_green', 'blue', 'on_green')

# all attributes available
attributes = ['bold', 'underline', 'reverse']
cprint('normal', end = ' | ')
for attr in attributes:
    if attr != 'reverse':
        cprint(attr, attrs = [attr], end = ' | ')
    else:
        cprint(attr, attrs = [attr])

# test all color and background
'''
print()
for textcolor in colors:
    for bkgcolor in colors:
        if textcolor != bkgcolor:
            cprint(textcolor + ', on_' + bkgcolor, textcolor, 'on_' + bkgcolor, end = ' | ')
    print()
'''