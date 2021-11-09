from Domain.vanzare import get_str, get_titlu, get_gen, get_pret, get_tip, creeaza_vanzare
from Logic.apply_discount import apply_discount
from Logic.change_genre import change_genre
from Logic.crud import create, read, update, delete
from Logic.distinct_titles import distinct_titles
from Logic.min_price import min_price
from Logic.sort_price import sort_price
from Logic.undo_redo import do_undo, do_redo


def show_menu():
    print('1. CRUD')
    print('2. Aplicare discount-uri pentru fiecare tip de reducere')
    print('3. Modificarea genului pentru un titlu dat')
    print('4. Determinarea pretului minim pentru fiecare gen')
    print('5. Ordonarea vanzarilor crescator dupa pret')
    print('6. Afisarea numarului de titluri distincte pentru fiecare gen')
    print('u. Undo')
    print('r. Redo')
    print('x. Exit')


def handle_add(vanzari, undo_list, redo_list):
    try:
        id_vanzare = int(input('Dati id-ul vanzarii: '))
        titlu = input('Dati titlul cartii: ')
        gen = input('Dati genul cartii: ')
        pret = float(input('Dati pretul cartii: '))
        tip = input('Dati tipul de reducere client al cartii: ')
        return create(vanzari, id_vanzare, titlu, gen, pret, tip, undo_list, redo_list)
    except ValueError as ve:
        print('Eroare: ', ve)

    return vanzari


def handle_show_all(vanzari):
    for vanzare in vanzari:
        print(get_str(vanzare))


def handle_show_details(vanzari):
    id_vanzare = int(input("Dati id-ul vanzarii pentru care vreti detalii: "))
    vanzare = read(vanzari, id_vanzare)
    print(f'Titlu carte: {get_titlu(vanzare)}')
    print(f'Gen carte: {get_gen(vanzare)}')
    print(f'Pret carte: {get_pret(vanzare)}')
    print(f'Tip reducere client pentru carte: {get_tip(vanzare)}')


def handle_update(vanzari, undo_list, redo_list):
    try:
        id_vanzare = int(input('Dati id-ul vanzarii care se actualizeaza: '))
        titlu = input('Dati noul titlu al cartii: ')
        gen = input('Dati noul gen al cartii: ')
        pret = float(input('Dati noul pret al cartii: '))
        tip = input('Dati noul tipul de reducere client al cartii: ')
        return update(vanzari, creeaza_vanzare(id_vanzare, titlu, gen, pret, tip), undo_list, redo_list)
    except ValueError as ve:
        print('Eroare:', ve)

    return vanzari


def handle_delete(vanzari, undo_list, redo_list):
    try:
        id_vanzare = int(input('Dati id-ul vanzarii pentru care se face stergerea: '))
        vanzari = delete(vanzari, id_vanzare, undo_list, redo_list)
        print('Stergea a fost efectuata cu succes')
        return vanzari
    except ValueError as ve:
        print('Eroare: ', ve)
    return vanzari


def handle_crud(vanzari, undo_list, redo_list):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('d. Detalii')
        print('b. Revenire')

        optiune = input('Optiune aleasa: ')
        if optiune == '1':
            vanzari = handle_add(vanzari, undo_list, redo_list)
        elif optiune == '2':
            vanzari = handle_update(vanzari, undo_list, redo_list)
        elif optiune == '3':
            vanzari = handle_delete(vanzari, undo_list, redo_list)
        elif optiune == 'a':
            handle_show_all(vanzari)
        elif optiune == 'd':
            handle_show_details(vanzari)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida')
    return vanzari


def handle_apply_discount(vanzari, undo_list, redo_list):
    vanzari = apply_discount(vanzari, undo_list, redo_list)
    print('Aplicarea reducerii a fost efectuata cu succes')
    return vanzari


def handle_change_genre(vanzari, undo_list, redo_list):
    try:
        titlu = input('Dati titlul cartii pe care doriti sa o modificati: ')
        gennou = input('Dati noul gen: ')
        vanzari = change_genre(vanzari, titlu, gennou, undo_list, redo_list)
        print('Modificarea genului a fost efectuata cu succes')
        return vanzari
    except ValueError as ve:
        print('Eroare: ', ve)
    return vanzari


def handle_min_price(vanzari):
    rezultat = min_price(vanzari)
    for gen in rezultat:
        print(f'Pretul minim pentru genul {gen} este {rezultat[gen]}')


def handle_sort_price(vanzari):
    vanzari = sort_price(vanzari)
    handle_show_all(vanzari)


def handle_distinct_titles(vanzari):
    rezultat = distinct_titles(vanzari)
    for gen in rezultat:
        print(f'Numarul de titluri distincte pentru genul {gen} este {rezultat[gen]}')


def handle_undo(vanzari, undo_list, redo_list):
    undo_result = do_undo(undo_list, redo_list, vanzari)
    if undo_result is not None:
        return undo_result
    return vanzari


def handle_redo(vanzari, undo_list, redo_list):
    redo_result = do_redo(undo_list, redo_list, vanzari)
    if redo_result is not None:
        return redo_result
    return vanzari


def run_ui(vanzari, undo_list, redo_list):
    while True:
        show_menu()
        optiune = input('Optiune aleasa: ')
        if optiune == '1':
            vanzari = handle_crud(vanzari, undo_list, redo_list)
        elif optiune == '2':
            vanzari = handle_apply_discount(vanzari, undo_list, redo_list)
        elif optiune == '3':
            vanzari = handle_change_genre(vanzari, undo_list, redo_list)
        elif optiune == '4':
            handle_min_price(vanzari)
        elif optiune == '5':
            handle_sort_price(vanzari)
        elif optiune == '6':
            handle_distinct_titles(vanzari)
        elif optiune == 'u':
            vanzari = handle_undo(vanzari, undo_list, redo_list)
        elif optiune == 'r':
            vanzari = handle_redo(vanzari, undo_list, redo_list)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')

    return vanzari
