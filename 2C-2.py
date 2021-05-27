def room_test(room):
    if len(room) > 3:
        print("The room is crowded!")
    else:
        print("The room is not crowded!")


crowded_list = ["Foo", "Bar", "Baz", "Foo", "Bar", "Baz"]
not_crowded = ["Foo", "Bar", "Baz"]

room_test(crowded_list)
room_test(not_crowded)
crowded_list = crowded_list[0:3]
room_test(crowded_list)  # should now be not crowded
