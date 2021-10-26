from Domain.vanzare import creeaza_vanzare, get_id


def create(lst_vanzari, id_vanzare: int, titlu_carte, gen_carte, pret, tip_reducere):
    """
    Adauga o noua vanzare in lista
    :param lst_vanzari: lista de vanzari
    :param id_vanzare: id-ul vanzarii noi
    :param titlu_carte: titlul cartii(vanzarii) noi
    :param gen_carte: genul cartii(vanzarii) noi
    :param pret: pretul cartii(vanzarii) noi
    :param tip_reducere: tipul de reducere a cartii(vanzarii) noi
    :return: o noua lista formata din lst_vanzari si noua vanzare adaugata
    """
    vanzare = creeaza_vanzare(id_vanzare, titlu_carte, gen_carte, pret, tip_reducere)
    return lst_vanzari + [vanzare]


def read(lst_vanzari, id_vanzare: int = None):
    """
    Citeste o vanzare din "baza de date"
    :param lst_vanzari: lista de vanzari
    :param id_vanzare: id-ul vanzarii dorite
    :return: vanzare cu id-ul id_vanzare sau lista cu toate vanzarile daca id_vanzare=None
    """
    vanzare_cu_id = None
    for vanzare in lst_vanzari:
        if get_id(vanzare) == id_vanzare:
            vanzare_cu_id = vanzare
    if vanzare_cu_id:
        return vanzare_cu_id
    return lst_vanzari


def update(lst_vanzari, new_vanzare):
    """
    Actualizeaza o vanzare
    :param lst_vanzari: lista de vanzari
    :param new_vanzare: vanzarea care se va actualiza
    :return: o lista cu vanzarea actualizata
    """
    new_vanzari = []
    for vanzare in lst_vanzari:
        if get_id(vanzare) != get_id(new_vanzare):
            new_vanzari.append(vanzare)
        else:
            new_vanzari.append(new_vanzare)
    return new_vanzari


def delete(lst_vanzari, id_vanzare: int):
    """
    Sterge o vanzare din "baza de date"
    :param lst_vanzari: lista de vanzari
    :param id_vanzare: id-ul vanzarii date spre stergere
    :return: o lista de vanzari fara vanzarea cu id-ul id_vanzare
    """
    new_vanzari = []
    for vanzare in lst_vanzari:
        if get_id(vanzare) != id_vanzare:
            new_vanzari.append(vanzare)

    return new_vanzari
