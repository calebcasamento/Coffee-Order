# Order taker
import coffee_shop

print(f'Welcome to {coffee_shop.shop_name}!')
print('Can I take your order?')

order = []
done = False

while done == False:
    print('Which item would you like?')
    
    for i in range(len(coffee_shop.menu_items)):
        print(f'\t[ {i} ] : {coffee_shop.menu_items[i]}')

    print('\t[ d ] : Done')
    selection = input('Enter a number or d for done: ')
    if selection.lower() == 'd':
        done = True
    else:
        selection = int(selection)
        print(f'That is a {coffee_shop.menu_items[selection]}')
        print('What size?')
        for i in range(len(coffee_shop.item_sizes)):
            print(f'\t[ {i} ] : {coffee_shop.item_sizes[i]}')
            #print('\t[ %i ] : %s' % (i,coffee_shop.item_sizes[i]))
            #print('\t[', i, '] :', coffee_shop.item_sizes[i])
        size = int(input('Enter a number from the list '))
        order.append((selection, size))

# Repeat the order back
print("\n\nOkay, here's your order")
for i in range(len(order)):
    size = f'{coffee_shop.item_sizes[order[i][1]]}'
    item = f'{coffee_shop.menu_items[order[i][0]]}'
    print(f'{size} {item}')
    
        
        
    





