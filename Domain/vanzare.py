def creeaza_vanzare(id_vanzare, titlu_carte, gen_carte, pret, tip_reducere):
    """
    Creeaza o vanzare
    :param id_vanzare: id-ul vanzarii(numar de vanzare), trebuie sa fie unic
    :param titlu_carte: titlul cartii(vanzarii)
    :param gen_carte: genul cartii(vanzarii)
    :param pret: pretul cartii(vanzarii)
    :param tip_reducere: tip reducere client (none, silver, gold) pentru carte(vanzare)
    :return:
    """
    return [
        id_vanzare,
        titlu_carte,
        gen_carte,
        pret,
        tip_reducere,
    ]


def get_id(vanzare):
    """
    Getter pentru id-ul vanzarii
    :param vanzare: vanzarea
    :return: id-ul vanzarii date ca parametru
    """
    return vanzare[0]


def get_titlu(vanzare):
    """
    Getter pentru titlu cartii(vanzarii)
    :param vanzare: vanzarea
    :return: titlul cartii(vanzarii) date ca parametru
    """
    return vanzare[1]


def get_gen(vanzare):
    """
    Getter pentru genul cartii(vanzarii)
    :param vanzare: vanzarea
    :return: genul cartii(vanzarii) date ca parametru
    """
    return vanzare[2]


def get_pret(vanzare):
    """
    Getter pentru pretul cartii(vanzarii)
    :param vanzare: vanzarea
    :return: pretul cartii(vanzarii) date ca parametru
    """
    return vanzare[3]


def get_tip(vanzare):
    """
    Getter pentru tipul de reducere client al cartii(vanzarii)
    :param vanzare: vanzarea
    :return: tipul de reducere al cartii(vanzarii) date ca parametru
    """
    return vanzare[4]

def get_str(vanzare):
    """
    Determina reprezentarea ca string a vanzarii
    :param vanzare: vanzarea
    :return: id-ul, titlul, genul, pretul si tipul reducere a vanzarii
    """
    return f'Vanzarea cu id-ul {get_id(vanzare)} este o carte cu titlul {get_titlu(vanzare)} si pretul {get_pret(vanzare)}.'