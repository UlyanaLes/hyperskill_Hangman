def what_to_do(instructions):
    my_list = instructions.strip().split()
    if my_list[0] == 'Simon' and my_list[1] == 'says':
        return f'I {instructions[11:]}'
    elif my_list[-2] == 'Simon' and my_list[-1] == 'says':
        return f'I {instructions[0:-11]}'
    else:
        return "I won't do it!"
