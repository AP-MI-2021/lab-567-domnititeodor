from Domain.vanzare import creeaza_vanzare, get_id
from Logic.sort_price import sort_price


def get_data():
    return [
        creeaza_vanzare(1, 'v1', 'gen1', 60, 'silver'),
        creeaza_vanzare(2, 'v2', 'gen1', 20, 'none'),
        creeaza_vanzare(3, 'v3', 'gen2', 12, 'gold'),
        creeaza_vanzare(4, 'v5', 'gen3', 23.02, 'none'),
    ]
def test_sort_price():
    vanzari = get_data()
    vanzari = sort_price(vanzari)
    assert len(vanzari) == 4
    assert get_id(vanzari[0]) == 3
    assert get_id(vanzari[1]) == 2
    assert get_id(vanzari[2]) == 4
    assert get_id(vanzari[3]) == 1