# write your code here
text = '         '



new_text_list = []
list_new = []
count = 0
for x in text:
    count += 1
    if count % 3 == 0:
        list_new.append(x)
        new_text_list.append(list_new)
        list_new = []
    else:
        list_new.append(x)

flag = True
while flag:
    print('-' * 9)

    print(f'| {new_text_list[0][0]} {new_text_list[0][1]} {new_text_list[0][2]} |')
    print(f'| {new_text_list[1][0]} {new_text_list[1][1]} {new_text_list[1][2]} |')
    print(f'| {new_text_list[2][0]} {new_text_list[2][1]} {new_text_list[2][2]} |')

    print('-' * 9)
    stroke = 'X'
    count_s = 1
    flag2 = True

    while flag2:

        if count_s % 2 == 1:
            stroke = 'X'
        else:
            stroke = '0'

        print('Enter the coordinates:', end='')
        move = input()
        new_list = move.split(' ')

        if new_list[0].isdigit() and new_list[1].isdigit():
            if 1 <= int(new_list[0]) <= 3 and 1 <= int(new_list[1]) <= 3:
                if new_text_list[int(new_list[0]) - 1][int(new_list[1]) - 1] == 'O' or \
                        new_text_list[int(new_list[0]) - 1][int(new_list[1]) - 1] == 'X':
                    print('This cell is occupied! Choose another one!')
                else:
                    new_text_list[int(new_list[0]) - 1][int(new_list[1]) - 1] = stroke

                    print('-' * 9)
                    print(f'| {new_text_list[0][0]} {new_text_list[0][1]} {new_text_list[0][2]} |')
                    print(f'| {new_text_list[1][0]} {new_text_list[1][1]} {new_text_list[1][2]} |')
                    print(f'| {new_text_list[2][0]} {new_text_list[2][1]} {new_text_list[2][2]} |')
                    print('-' * 9)
            else:
                print('Coordinates should be from 1 to 3!')
                continue
        else:
            print('You should enter numbers!')

        list_true = [new_text_list[0][0] + new_text_list[0][1] + new_text_list[0][2],
                     new_text_list[1][0] + new_text_list[1][1] + new_text_list[1][2],
                     new_text_list[2][0] + new_text_list[2][1] + new_text_list[2][2],
                     new_text_list[0][0] + new_text_list[1][0] + new_text_list[2][0],
                     new_text_list[1][0] + new_text_list[1][1] + new_text_list[1][2],
                     new_text_list[2][0] + new_text_list[2][1] + new_text_list[2][2],
                     new_text_list[0][0] + new_text_list[1][1] + new_text_list[2][2],
                     new_text_list[2][2] + new_text_list[1][1] + new_text_list[0][2]]

        new_stroke = ''
        
        for elen in new_text_list:
            for elem in elen:
                new_stroke += elem
        
        if 'XXX' in list_true:
            print('X wins')
            flag2 = False
            flag = False
        elif '000' in list_true:
            print('0 wins')
            flag2 = False
            flag = False
        elif new_stroke.count('X') + new_stroke.count('0') == 9:
            print('Draw')
            flag2 = False
            flag = False

        count += 1
