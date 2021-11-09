from Domain.vanzare import get_tip, creeaza_vanzare, get_id, get_titlu, get_pret, get_gen


def apply_discount(lst_vanzari, undo_list, redo_list):
    """
    Reduce pretul unei vanzari in functie de tipul de reducere pe care il are (silver - 5% , gold - 10%)
    :param lst_vanzari: lista de vanzari
    :param undo_list: o lista care memoreaza lista de vanzari inainte de modificari
    :param redo_list: o lista care memoreaza lista de vanzari dupa modificari
    :return: lista de vanzari dupa reducerea pretului fiecarui element
    """
    new_vanzari = []
    for vanzare in lst_vanzari:
        if get_tip(vanzare) == 'silver':
            n_vanzare = creeaza_vanzare(
                get_id(vanzare),
                get_titlu(vanzare),
                get_gen(vanzare),
                (get_pret(vanzare) - (0.05 * get_pret(vanzare))),
                get_tip(vanzare)
            )
            new_vanzari.append(n_vanzare)
        elif get_tip(vanzare) == 'gold':
            n_vanzare = creeaza_vanzare(
                get_id(vanzare),
                get_titlu(vanzare),
                get_gen(vanzare),
                (get_pret(vanzare) - (0.1 * get_pret(vanzare))),
                get_tip(vanzare)
            )
            new_vanzari.append(n_vanzare)
        else:
            new_vanzari.append(vanzare)

    undo_list.append(lst_vanzari)
    redo_list.clear()
    return new_vanzari
