def display_message():
    '''Criar sempre um comentário logo a seguir à criação de uma função para
    docuemntar corretamente'''
    print("Iam learning function in this chapter.")

display_message()

print("\n ----- \n")

def favourite_book(title):
    '''Cria uma frase com o titulo dado pelo o utilizador'''
    print(f"One of my favourite books is '{title}'.")

favourite_book("A sombra do Vento")

print("\n ----- \n")

def make_pizza(*toppings):
    ''' Return num número indefinido de toppings.
        Ao fazer desta maneira, o python vai criar um tuple'''
    print(toppings)

    print("\n -- with for loop -- \n")
    print("Making a pizza with the following toppings: ")
    for topping in toppings:
        print(f" - {topping}")

make_pizza("pepperoni")
make_pizza("pepperoni", "green peppers", "extra cheese")