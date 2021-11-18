#I learn set and dict comprehension and got skills about it use
# This program creates dict with string keys and values in set
#input: Pushkin: Ballada about fishiner
#       Pushkin: Evgeniy Onegin
#output: {'Pushkin: {'Ballada about fishiner','Evgeniy Onegin'}'}



lst_in = list(map(str.strip, sys.stdin.readlines()))

new_lst = [i.split(': ') for i in lst_in]
d = {key:{set_value for set_key, set_value in new_lst if set_key == key} for key,  i in new_lst}
