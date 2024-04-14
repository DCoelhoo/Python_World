from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text()

#remove the extra blank line
contents = contents.rstrip() 

lines = contents.splitlines()
pi_string = ""

for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string}...")
print(len(pi_string))



