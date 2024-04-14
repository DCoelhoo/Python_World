from _city_functions import city_country

def test_city_country():
    '''Do strings like "Santiago, Chile" work? '''
    display = city_country("Santiago", "Chile")
    assert display == "Santiago, Chile"

def test_city_country_population():
    '''Do strings like "Santiago, Chile -- population" work? '''
    display = city_country("Santiago", "Chile", 5_000_000)
    assert display == "Santiago, Chile -- 5000000"