rooms = {} # empty dictionary, key is guest name, value is the room number
while True:
    print('Welcome to the Hotel California')
    print('1. Check in')
    print('2. Check out')
    print('3. Change room')
    print('4. Show all rooms')
    print('5. Exit')

    choice = int(input('Enter your choice: '))
    if choice == 1:
        # TODO: Check in, ask guest name and room number then add to rooms
        name = input('What is your name: ')
        room_no = input('Which room number do you book: ')
        if name not in rooms:
            rooms[name] = room_no
            print(f'Welcome {name}, your room is {room_no}')
        else:
            print(f'{name} is already checked in')
    elif choice == 2:
        # TODO: Check out, ask guest name then remove from rooms
        name = input('What is your name: ')
        if name in rooms:
            del rooms[name]
            print(f'Good bye {name}. See you again')
    elif choice == 3:
        # TODO: Change room, ask guest name and new room number then update rooms
        name = input('What is your name: ')
        if name in rooms:
            room_no = input('Which room number do you want to change: ')
            rooms[name] = room_no
            print(f'Your new room is {room_no}')
        else:
            print(f'{name} is not checked in')
    elif choice == 4:
        print('Current guests & rooms')
        print(rooms)
    elif choice == 5:
        print('Good bye')
        break
    else:
        print('Invalid choice')