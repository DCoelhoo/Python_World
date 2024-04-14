from pathlib import Path

def read_files(path):
    '''Reads files'''

    try:
        print(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        pass

dogs = Path("dogs.txt")
read_files(dogs)

print("\n ----- \n")

cats = Path("cats.txt")
read_files(cats)