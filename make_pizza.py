''' Este ficheiro foi criado para importar e usar as funções criadas no 
    ficheiro pizza.py '''

import pizza

pizza.make_pizza(40, "pepperoni")
pizza.make_pizza(20, "pepperoni", "ham", "cheese")

''' Podemos importar os modules das seguintes formas:
        import pizza as p
        from pizza import make_pizza
        from pizza import make_pizza as mp
        from pizza import *
        
    Ou podemos importar desta forma.'''