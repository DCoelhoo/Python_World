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

print("\n----------------\n")

cities = {
    "Toquio" : {
        "country" : "Japão",
        "population" : 14_000_000,
        "fact" : "Tóquio é a maior área metropolitana do mundo em termos de "
            "população, tornando-se uma das cidades mais populosas e dinâmicas do planeta.",
    },
    "Cidade do México" : {
        "country" : "México",
        "population" : 9_000_000,
        "fact" : " A Cidade do México é uma das cidades mais antigas das Américas,"
            " fundada pelos Astecas no século XIV como Tenochtitlán. Sua história é "
            "rica e diversa, refletindo-se na arquitetura, cultura e tradições da cidade",
    },
    "Lagos" : {
        "country" : "Nigéria",
        "population" : 14_000_000,
        "fact" : "Lagos é o centro financeiro da Nigéria e uma das cidades de" 
            "crescimento mais rápido no mundo. É conhecida por sua energia vibrante,"
            "diversidade cultural e como um importante centro de comércio na África Ocidental.",
    },
}

for city, info in cities.items():
    print(f"\n{city.title()}")
    print(f"País:{info['country'].title()}")
    print(f"População:{info['population']}")
    print(f"Fact:{info['fact']}")

