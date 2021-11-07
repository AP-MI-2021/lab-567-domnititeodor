from Domain.vanzare import creeaza_vanzare
from Logic.distinct_titles import distinct_titles


def get_data():
    return [
        creeaza_vanzare(1, 'v1', 'gen1', 60, 'silver'),
        creeaza_vanzare(2, 'v2', 'gen2', 20, 'none'),
        creeaza_vanzare(3, 'v3', 'gen2', 12, 'gold'),
        creeaza_vanzare(4, 'v4', 'gen4', 34, 'silver'),
        creeaza_vanzare(5, 'v2', 'gen2', 34, 'silver'),
        creeaza_vanzare(6, 'v4', 'gen4', 34, 'silver'),
        creeaza_vanzare(7, 'v4', 'gen4', 34, 'silver'),
    ]


def test_distinct_titles():
    vanzari = get_data()
    rezultat = distinct_titles(vanzari)
    assert rezultat['gen1'] == 1
    assert rezultat['gen2'] == 2
    assert rezultat['gen4'] == 1
