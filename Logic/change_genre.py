from Domain.vanzare import get_titlu, get_id, creeaza_vanzare, get_pret, get_tip


def change_genre(lst_vanzari, titlu, gen_nou, undo_list, redo_list):
    """
    Modifica genul unui titlu dat din lista de vanzari
    :param lst_vanzari: lista de vanzari
    :param titlu: titlul dat spre modificare
    :param gen_nou: noul gen al titlui
    :param undo_list: o lista care memoreaza lista de vanzari inainte de modificari
    :param redo_list: o lista care memoreaza lista de vanzari dupa modificari
    :return: o lista de vanzari in care titlul are genul nou dat
    """
    if title_in_lst(lst_vanzari,titlu) is None:
        raise ValueError('Ati introdus un titlu care nu se afla in lista vanzarilor')
    new_vanzari = []
    for vanzare in lst_vanzari:
        if get_titlu(vanzare) == titlu:
            n_vanzare = creeaza_vanzare(
                get_id(vanzare),
                get_titlu(vanzare),
                gen_nou,
                get_pret(vanzare),
                get_tip(vanzare)
            )
            new_vanzari.append(n_vanzare)
        else:
            new_vanzari.append(vanzare)
    undo_list.append(lst_vanzari)
    redo_list.clear()
    return new_vanzari



def title_in_lst(lst_vanzari, titlu):
    """
    Verifica daca titlul dat se gaseste in lista de vanzari
    :param lst_vanzari: lista de vanzari
    :param titlu: titlul dat spre verificare
    :return: id-ul vanzarii, daca titlul exista in lista sau None in caz contrar
    """
    vanzare_cu_id = None
    for vanzare in lst_vanzari:
        if get_titlu(vanzare) == titlu:
            vanzare_cu_id = get_id(vanzare)
    if vanzare_cu_id:
        return vanzare_cu_id
    return None
