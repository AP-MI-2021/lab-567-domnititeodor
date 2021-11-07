from Domain.vanzare import get_gen, get_pret


def min_price(lst_vanzari):
    """
    Determina pretul minim pentru fiecare gen
    :param lista: lista de vanzari
    :return: un dictionar care contine pentru fiecare cheie (gen) pretul minim
    """
    rezultat = {}
    for vanzare in lst_vanzari:
        gen = get_gen(vanzare)
        pret = get_pret(vanzare)
        if gen in rezultat:
            if pret < rezultat[gen]:
                rezultat[gen] = pret
        else:
            rezultat[gen] = pret
    return rezultat