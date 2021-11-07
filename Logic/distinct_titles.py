from Domain.vanzare import get_gen, get_titlu


def distinct_titles(lst_vanzari):
    """
    Determina numarul de titluri distincte pentru fiecare gen
    :param lst_vanzari: lista de vanzari
    :return: un dictionar care contine pentru fiecare cheie (gen) numarul de titluri distincte
    """
    rezultat1 = {}
    rezultat2 = {}
    for vanzare in lst_vanzari:
        gen = get_gen(vanzare)
        titlu = get_titlu(vanzare)
        if gen in rezultat1:
            if titlu not in rezultat2[gen]:
                rezultat1[gen] = rezultat1[gen] + 1
                all_titles = rezultat2[gen] + titlu
                rezultat2[gen] = all_titles
        else:
            rezultat1[gen] = 1
            rezultat2[gen] = titlu
    return rezultat1
