rivers = {
    "nile" : "egypt",
    "tejo" : "portugal",
    "mississipi" : "mexico",
    "lena" : "russia",
    "douro" : "portugal",
    "sena" : "portugal"
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\n----------------\n")

for river in rivers.keys():
    print(f"River's name: {river.title()}")

print("\n----------------\n")

for country in rivers.values():
    print(f"Country: {country.title()}")

#print the dictionary withtout duplicates
print("\n----------------\n")

for country in set(rivers.values()):
    print(f"Country: {country.title()}")