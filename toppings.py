toppings = ['mushrooms','green peppers','extra chesse']
requested_toppings = ['french fries','pineapple']
for topping in toppings:
    if topping == 'green peppers':
        print('sorry we ran out of green peppers.' )
    else:
        print(f'Adding {topping}.')
for topping in requested_toppings:
    if topping in toppings:
        print(f'Added {topping}.')
    else:
        print('we donot have it.')
print('\n pizza made. ')


