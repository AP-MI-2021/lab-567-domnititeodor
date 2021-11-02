from Domain.vanzare import creeaza_vanzare, get_pret
from Logic.apply_discount import apply_discount


def get_data():
    return [
        creeaza_vanzare(1, 'v1', 'gen1', 60, 'silver'),
        creeaza_vanzare(2, 'v2', 'gen2', 20, 'none'),
        creeaza_vanzare(3, 'v3', 'gen3', 12, 'gold'),
        creeaza_vanzare(4, 'v4', 'gen4', 34, 'silver'),
    ]

def test_discount():
    vanzari = get_data()
    new_vanzari = apply_discount(vanzari)
    assert len(new_vanzari) == 4
    assert get_pret(new_vanzari[0]) == 57
    assert get_pret(new_vanzari[1]) == 20
    assert get_pret(new_vanzari[2]) == 10.8
