#!/usr/bin/env python3
import sys

donors = [("Rufio"), [100, 200, 200],
          ("Maggie"), [100, 2, 3000],
          ("Gus"), [100, 32, 33222],
          ("Kramer"), [10, 87, 886],
          ("Polly"), [432, 32, 7896]
         ]


def thank_you():
    get_donors_name = input("Please enter your full name: ")
    
    for i in donors:
        if i == get_donors_name:
            print(f"match with {i}")
        else:
            print("no dice")


def gen_stats(donor):
    donations = donor[1]
    total = sum(donations)
    num = len(donations)
    stats = (donor[0], total, num, total / num) 
    
    return stats

def report():
    print("Create a report")


def quit():
    sys.exit(0)    


def main_menu():
    while True:
        answer = input("""What you would you like to do?
    Pick One:
    1: Send a thank you
    2: Create a report
    3: Quit
    >>> """)
        print(f"You selected {answer}")
        print(answer)
        answer = answer.strip()
        if answer == "1":
            thank_you()
        elif answer == "2":
            report()
        elif answer == "3":
            quit()
        else:
            print("Please answer 1, 2, or 3")



if __name__ == "__main__":
    print("Welcome to the Mailroom")

    donor = ("fred flinstone"), [100, 50, 600]
    # assert gen_stats(donor) == ("fred flinstone"), [750, 3, 250.0] 

    main_menu()
