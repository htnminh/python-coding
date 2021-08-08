import the_module

f = open('the_input.txt', 'r')
input_string = f.readline()
lst = [int(x) for x in input_string.split()]
print(the_module.the_sum_of(lst))
input('Enter to continue')