def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-uinch pizza with the following topppings:")
    for topping in toppings:
        print("- " + topping)
