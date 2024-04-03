def make_sandwich(*ingredients):
    ''' Return nos ingredientes da sandwich'''

    print("\nA sandwich vai ser feita com:")

    for ingredient in ingredients:
        print(f" - {ingredient}")

sandwich1 = make_sandwich("cheese")
sandwich1 = make_sandwich("cheese", "ham")
sandwich1 = make_sandwich("cheese", "ham", "butter")


def build_profile(first, last, **user_info):
    ''' Cria um dicionário com os dados todos que o user der, alem do 1º e 
        último nome.'''
    
    user_info['First Name'] = first
    user_info['Last Name'] = last

    return user_info

user_profile = build_profile("Diogo", "Gonçalves", 
                             idade = 22, altura = 1.69, 
                             gender = "male")

print(user_profile)

