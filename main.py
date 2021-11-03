from Logic.crud import create
from Tests.test_change_genre import test_alt_genre
from Tests.test_crud import test_crud
from Tests.test_discount import test_discount
from UserInterface.command_line_console import new_menu
from UserInterface.console import run_ui

def menus():
    print('1. Meniul standard')
    print('2. Meniul nou')
    print('x. Exit')

def main():
    vanzari = []
    vanzari = create(vanzari, 1, 'Dune', 'SF', 25.99, 'silver')
    vanzari = create(vanzari, 2, 'Harry Potter', 'Fantasy', 24, 'none')
    vanzari = create(vanzari, 3, 'Animal Farm', 'Political Satire', 12.50, 'gold')
    vanzari = create(vanzari, 4, 'Shining', 'Horror', 27.49, 'silver')
    vanzari = create(vanzari, 5, 'A game of thrones', 'Fantasy', 60, 'silver')
    vanzari = create(vanzari, 6, 'Narnia', 'Fantasy', 13.99, 'gold')

    while True:
        menus()
        optiune = input('Alegeti meniul: ')
        if optiune == '1':
            vanzari = run_ui(vanzari)
        elif optiune == '2':
            vanzari = new_menu(vanzari)
        elif optiune == 'x':
            break
        else:
            print("Optiune invalida ")


if __name__ == '__main__':
    test_crud()
    test_discount()
    test_alt_genre()
    main()
