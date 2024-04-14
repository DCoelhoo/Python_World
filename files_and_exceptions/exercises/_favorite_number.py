from pathlib import Path
import json

path = Path("favorite_number.json")

if path.exists():
    contents = path.read_text()
    fav_number = json.loads(contents)
    print(f"Your favorite number is {fav_number}")
else: 
    fav_number = input("What is your favorite number? ")
    contents = json.dumps(fav_number)
    path.write_text(contents)
    print("We will save your favorite number.")
