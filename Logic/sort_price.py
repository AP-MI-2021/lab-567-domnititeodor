from Domain.vanzare import get_pret


def sort_price(lst_vanzari):
    """
    Ordoneaza crescator lista de vanzari dupa pret
    :param lst_vanzari: lista de vanzari
    :return: lista de vanzari ordonata crescator dupa pret
    """
    return sorted(lst_vanzari, key=lambda vanzare: get_pret(vanzare))