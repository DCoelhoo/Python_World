def make_shirt(display_message = "Python", size ="L"):
    '''Recebe a mensagem e o tamanho da t shirt (dada) pelo utilizador.'''
    print(f"Size: {size} --- Message: {display_message}")

make_shirt("AAAAAAAAA", "S")
make_shirt(display_message="This is L.")
make_shirt(display_message="This is XXL.", size = "XXL")
make_shirt(size = "M")
make_shirt()

print("\n ------------------ \n")

def city_country(city, country = "Portugal"):
    '''Devolve o nome a da cidade e o pais.'''
    result = f"{city}, {country}"
    return result.title()

pair1 = city_country("Lisbon")
pair2 = city_country("Madrid", "Spain")
pair3 = city_country("Tokyo", "Japan")

print(pair1)
print(pair2)
print(pair3)

print("\n ------------------ \n")

def make_album(artist_name, album_title, nr_songs = None):
    '''Return num dicionário com o nome do artista e album'''

    if nr_songs:
        album = {
            "artist" : artist_name, 
            "album" : album_title,
            "nr of songs" : nr_songs,
        }
    else:
            album = {
            "artist" : artist_name, 
            "album" : album_title,
        }

    return print(album);

make_album("artista", "disco1")
make_album("artista1", "disco2")
make_album("artista2", "disco3", 10)

print("\n ------------------ \n")

while True:
    print("\n New album")
    print("(press 'q' to finish the program)")

    artist = input("Artist name: ").lower()
    
    if artist == 'q':
        break
    
    album = input("Album name: ").lower()
    
    if album == 'q':
        break

    make_album(artist, album)
