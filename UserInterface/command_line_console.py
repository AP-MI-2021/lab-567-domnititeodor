from Domain.vanzare import creeaza_vanzare
from Logic.crud import create, delete, update
from UserInterface.console import handle_show_all


def read_list():
    lst = []
    lst_str = input("Introduceti comanda respectand instructiunile date: ")
    lst_str_split = lst_str.split('; ')
    for comanda in lst_str_split:
        lst.append(comanda)
    return lst


def handle_newadd(vanzari, comanda):
    try:
        id = int(comanda[1])
        titlu = comanda[2]
        gen = comanda[3]
        pret = float(comanda[4])
        tip = comanda[5]
        return create(vanzari, id, titlu, gen, pret, tip)
    except ValueError as ve:
        print('Eroare: ', ve)

    return vanzari


def handle_newdelete(vanzari, comanda):
    try:
        id = int(comanda[1])
        vanzari = delete(vanzari, id)
        return vanzari
    except ValueError as ve:
        print('Eroare: ', ve)
    return vanzari


def handle_newupdate(vanzari, comanda):
    try:
        id = int(comanda[1])
        titlu = comanda[2]
        gen = comanda[3]
        pret = float(comanda[4])
        tip = comanda[5]
        return update(vanzari, creeaza_vanzare(id, titlu, gen, pret, tip))
    except ValueError as ve:
        print('Eroare:', ve)
    return vanzari


def new_menu(vanzari):
    while True:
        print("Intr-o linie de comanda se vor scrie comenzile "
              "care se vor aplica listei, separate prin ';', elementele acestora fiind separate prin ','.")
        print("Atentie ! Comanda se face scrie cu majuscula si dupa fiecare separator(; si ,) se va pune un spatiu.")
        print("O comanda care nu se regaseste in lista de mai jos nu va duce la modificarea listei.")
        print("O comanda trebuie sa aiba toate campurile nenule \n ")

        print("1.Pentru adaugare in lista: Adaugare, id_vanzare(valoare intreaga), titlu, gen, "
              "pret(valoare reala), tip(none, silver sau gold)")
        print("2.Pentru stergerea unei vanzari: Sterge, id_vanzare(valoare intreaga)")
        print("3.Pentru modificarea unei vanzari: Modificare, id_vanzare(valoare intreaga), titlu, gen, "
              "pret(valoare reala), tip(none, silver sau gold)")
        print("4.Pentru afisarea tuturor vanzarilor: ShowAll")
        print("5. Pentru a iesire din meniu: Exit (la final)")
        lst_cmd = read_list()
        for comanda in lst_cmd:
            comanda = comanda.split(', ')
            if (comanda[0] == 'Adaugare'):
                vanzari = handle_newadd(vanzari, comanda)
            elif (comanda[0] == 'Sterge'):
                vanzari = handle_newdelete(vanzari, comanda)
            elif (comanda[0] == 'Modificare'):
                vanzari = handle_newupdate(vanzari, comanda)
            elif (comanda[0] == 'ShowAll'):
                handle_show_all(vanzari)
        if 'Exit' in lst_cmd:
            break
