from Domain.vanzare import creeaza_vanzare
from Logic.min_price import min_price


def get_data():
    return [
        creeaza_vanzare(1, 'v1', 'gen1', 60, 'silver'),
        creeaza_vanzare(2, 'v2', 'gen1', 20, 'none'),
        creeaza_vanzare(3, 'v3', 'gen2', 12, 'gold'),
        creeaza_vanzare(4, 'v4', 'gen2', 34, 'silver'),
        creeaza_vanzare(5, 'v5', 'gen3', 23.02, 'none'),
    ]

def test_min_price():
    vanzari = get_data()
    rezultat = min_price(vanzari)
    assert rezultat['gen1'] == 20
    assert rezultat['gen2'] == 12
    assert rezultat['gen3'] == 23.02