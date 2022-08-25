my_list = []
for my_element in my_iterable:
    if my_condition:
        # 'my_expression' usually contains 'my_element'
        my_list.append(my_expression)

my_list = [my_expression for my_element in my_iterable if my_condition]
