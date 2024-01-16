import pandas as pd

rooms_cost = {"Dulex Suite": 1000, "King  Suite": 3000, "Queen Suite": 2000}
rooms_available = {"Dulex Suite": 0, "King  Suite": 0, "Queen Suite": 0}
reviews = []
bookings = []


def get_availability() -> None:
    for key in rooms_available:
        print("Room: {}   Availability: {}   Room Cost: {}".format(
            key, rooms_available[key], rooms_cost[key]))


print("**************************")
print("---Welcome to Taj Hotel---")
print("**************************")
while True:
    print("**************************")
    response = input(
        'What would you like do: \nCheck Availability__(A) \nBook A Room_________(B) \nView Bookings_______(V) \nLeave A Review______(L) \nRead Reviews________(R) \nQuit________________(Q) \n: '
    ).lower()
    print("**************************")
    valid_responses = ['a', 'b', 'v', 'c', 'l', 'q']
    if response == 'a':
        print("**************************")
        print("Please find the available rooms:")
        get_availability()
        print("**************************")
    elif response == 'b':
        print("********************************")
        room_selection = 'Please select room '
        no_rooms = 0
        for key in rooms_available:
            rooms = rooms_available[key]
            no_rooms = no_rooms + rooms
            if rooms > 0:
                if key == 'Dulex Suite':
                    room_selection = room_selection + " Dulex(D)/"
                elif key == 'King  Suite':
                    room_selection = room_selection + " King(K)/"
                else:
                    room_selection = room_selection + " Queen(Q)/"
        if no_rooms == 0:
            print("Sorry no rooms available.")
        else:
            print("Please find the available rooms:")
            room_type = input(room_selection + ': ').lower()
            if room_type == 'd':
                rooms_available[
                    "Dulex Suite"] = rooms_available["Dulex Suite"] - 1
                name = input("Enter your name: ")
                emailid = input("Enter emailid: ")
                bookings.append([name, emailid, "Dulex Suite"])
                print(
                    "You have successfully booked a room {}. Thanks for choicing Taj."
                    .format(name))
            elif room_type == 'k':
                rooms_available[
                    "King  Suite"] = rooms_available["King  Suite"] - 1
                name = input("Enter your name: ")
                emailid = input("Enter emailid: ")
                bookings.append([name, emailid, "King  Suite"])
                print(
                    "You have successfully booked a room {}. Thanks for choicing Taj."
                    .format(name))
            elif room_type == 'q':
                rooms_available[
                    "Queen Suite"] = rooms_available["Queen Suite"] - 1
                name = input("Enter your name: ")
                emailid = input("Enter emailid: ")
                bookings.append([name, emailid, "Queen Suite"])
                print(
                    "You have successfully booked a room {}. Thanks for choicing Taj."
                    .format(name))
            else:
                print("Sorry invalid room selection, lets start over.")
        print("********************************")
    elif response == 'l':
        print("********************************")
        print("Your review is appreciated:")
        name = input("Enter name: ")
        emailid = input("Enter emailid: ")
        comment = input("Enter Review: ")
        reviews.append([name, emailid, comment])
        print("Thanks for your review. Our team will reach out to you.")
        print("********************************")
    elif response == 'r':
        print("********************************")
        print("Reviews: ")
        for review in reviews:
            print("Name: ", review[0])
            print("Emailid: ", review[1])
            print("Review: ", review[2])
        print("End of reviews.")
        print("********************************")
    elif response == 'v':
        print("********************************")
        print("Bookings: ")
        for book in bookings:
            print("Name: {} Emailid: {} Room: {}".format(
                book[0], book[1], book[2]))
        print("End of Bookings.")
        print("********************************")
    elif response == 'q':
        print("*************************************************")
        print("Thanks visiting us. Hope we can service you soon.")
        print("*************************************************")
        exit()
    else:
        print("Sorry invalid choice selected, lets start over.")