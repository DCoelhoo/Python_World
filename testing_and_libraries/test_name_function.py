from name_function import get_formatted_name

def test_first_last_name():
    '''For names like "Diogo Gonçalves" work? '''
    formatted_name = get_formatted_name("Diogo", "goncalves")
    assert formatted_name == "Diogo Goncalves"

def test_first_last_middle_name():
    '''For names like "Diogo Coelho Gonçalves" work? '''
    formatted_name = get_formatted_name("Diogo", "goncalves", "coelho")
    assert formatted_name == "Diogo Coelho Goncalves"