''' Este ficheiro foi criado para testes a importação de funções de ficheiros
    diferentes. As funções criadas neste ficheiro vão ser utilizadas no
    ficheiro make_pizza.py '''

def make_pizza(size, *toppings):
    ''' Summarize the pizza we are about to make '''
    print(f"\n A fazer uma pizza com {size} de diametro com os seguintes ingredientes:")

    for topping in toppings:
        print(f"- {topping}")