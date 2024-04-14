from pathlib import Path

path = Path("guest_book.txt")
active = True
guest_list = ""

while active:

    msg = input("Tell me your name!(Write 'quit' to end the program) -- ")

    if msg == "quit":
        active = False
    else:
        print("Name added to the guest book!")
        print("\n----\n")
        guest_list += f"{msg}\n"

path.write_text(guest_list)        