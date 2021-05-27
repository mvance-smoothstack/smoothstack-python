def room_test(room):
    if len(room) >= 6:
        print("There's a mob in the room!")
    elif 6 > len(room) >= 3:
        print("The room is crowded!")
    elif 3 > len(room) >= 1:
        print("The room is not crowded!")
    elif len(room) == 0:
        print("The room is empty.")


the_room = ["Foo", "Bar", "Baz", "Foo", "Bar", "Baz"]

room_test(the_room)
the_room = the_room[0:5]  # last two out of room
room_test(the_room)
the_room = the_room[0:2]  # three more out of room
room_test(the_room)
the_room = the_room[0:0]  # room is now empty
room_test(the_room)
