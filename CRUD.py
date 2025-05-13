print('Welcome!')

lista = ['Moacir', 'Cadmiel']

first_question = input('What do you want to do? (C, R, U, D): ')
first_question_low = first_question.lower()

if first_question_low == 'c':
    name = input('Enter the name to create: ')
    lista.append(name)
    print(f'{name} added!')

elif first_question_low == 'r':
    name = input('Enter the name to read (search): ')
    if name in lista:
        print(f'{name} is in the list.')
    else:
        print(f'{name} not found.')

elif first_question_low == 'u':
    old_name = input('Enter the name to update: ')
    if old_name in lista:
        new_name = input('Enter the new name: ')
        index = lista.index(old_name)
        lista[index] = new_name
        print(f'{old_name} updated to {new_name}.')
    else:
        print(f'{old_name} not found.')

elif first_question_low == 'd':
    name = input('Enter the name to delete: ')
    if name in lista:
        lista.remove(name)
        print(f'{name} removed!')
    else:
        print(f'{name} not found.')

else:
    print('Invalid option!')

print('Current list:', lista)
