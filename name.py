name = "diogo goncalves"
print(name.title())

first_name = "alexandre"
last_name = "coelho"
full_name = f"{first_name} {last_name}"
print(full_name.title())

#To add a Tab
print("\t" + name)

#To add a Newline
print("\n" + last_name + "\n" + full_name)

#Stripping Whitespaces
favorite_language = "   python    "
print(favorite_language.rstrip()) #right strip
print(favorite_language.lstrip()) #left strip   
print(favorite_language.strip()) #both sides

#removing Prefixes
google_url = "https://www.google.com/"
print(google_url.removeprefix("https://"))