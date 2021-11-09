from Domain.vanzare import creeaza_vanzare, get_id


def create(lst_vanzari, id_vanzare: int, titlu_carte, gen_carte, pret, tip_reducere, undo_list: list, redo_list: list):
    """
    Adauga o noua vanzare in lista
    :param lst_vanzari: lista de vanzari
    :param id_vanzare: id-ul vanzarii noi
    :param titlu_carte: titlul cartii(vanzarii) noi
    :param gen_carte: genul cartii(vanzarii) noi
    :param pret: pretul cartii(vanzarii) noi
    :param tip_reducere: tipul de reducere a cartii(vanzarii) noi
    :param undo_list: o lista care memoreaza lista de vanzari inainte de modificari
    :param redo_list: o lista care memoreaza lista de vanzari dupa modificari
    :return: o noua lista formata din lst_vanzari si noua vanzare adaugata
    """
    if read(lst_vanzari, id_vanzare) is not None:
        raise ValueError(f'Exista deja o vanzare cu id-ul {id_vanzare}')
    if tip_reducere != 'silver' and tip_reducere != 'gold' and tip_reducere != 'none':
        raise ValueError('Ati introdus un tip de reducere care nu exista')
    if pret < 0:
        raise ValueError('Pretul nu poate sa fie negativ')
    vanzare = creeaza_vanzare(id_vanzare, titlu_carte, gen_carte, pret, tip_reducere)
    undo_list.append(lst_vanzari)
    redo_list.clear()
    return lst_vanzari + [vanzare]


def read(lst_vanzari, id_vanzare: int = None):
    """
    Citeste o vanzare din "baza de date"
    :param lst_vanzari: lista de vanzari
    :param id_vanzare: id-ul vanzarii dorite
    :return: vanzare cu id-ul id_vanzare (daca exista),
             lista cu toate vanzarile daca id_vanzare=None si
             None daca nu exista vanzare cu id_vanzare
    """
    if not id_vanzare:
        return lst_vanzari
    vanzare_cu_id = None
    for vanzare in lst_vanzari:
        if get_id(vanzare) == id_vanzare:
            vanzare_cu_id = vanzare
    if vanzare_cu_id:
        return vanzare_cu_id
    return None


def update(lst_vanzari, new_vanzare, undo_list, redo_list):
    """
    Actualizeaza o vanzare
    :param lst_vanzari: lista de vanzari
    :param new_vanzare: vanzarea care se va actualiza
    :param undo_list: o lista care memoreaza lista de vanzari inainte de modificari
    :param redo_list: o lista care memoreaza lista de vanzari dupa modificari
    :return: o lista cu vanzarea actualizata
    """
    if read(lst_vanzari, get_id(new_vanzare)) is None:
        raise ValueError(f'Nu exista o vanzare cu id-ul {get_id(new_vanzare)} pe care sa o actualizam')
    new_vanzari = []
    for vanzare in lst_vanzari:
        if get_id(vanzare) != get_id(new_vanzare):
            new_vanzari.append(vanzare)
        else:
            new_vanzari.append(new_vanzare)

    undo_list.append(lst_vanzari)
    redo_list.clear()
    return new_vanzari


def delete(lst_vanzari, id_vanzare: int, undo_list, redo_list):
    """
    Sterge o vanzare din "baza de date"
    :param lst_vanzari: lista de vanzari
    :param id_vanzare: id-ul vanzarii date spre stergere
    :param undo_list: o lista care memoreaza lista de vanzari inainte de modificari
    :param redo_list: o lista care memoreaza lista de vanzari dupa modificari
    :return: o lista de vanzari fara vanzarea cu id-ul id_vanzare
    """
    if read(lst_vanzari, id_vanzare) is None:
        raise ValueError(f'Nu exista o vanzare cu id-ul {id_vanzare} pe care sa o stergem')
    new_vanzari = []
    for vanzare in lst_vanzari:
        if get_id(vanzare) != id_vanzare:
            new_vanzari.append(vanzare)

    undo_list.append(lst_vanzari)
    redo_list.clear()
    return new_vanzari
