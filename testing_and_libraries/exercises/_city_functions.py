def city_country(city, country, population = ""):
    '''Returns City and country '''

    if population:
        display = f"{city}, {country} -- {population}"
    else:
        display = f"{city}, {country}"

    return display