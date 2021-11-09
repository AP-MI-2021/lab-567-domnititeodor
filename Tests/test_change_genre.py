from Domain.vanzare import get_gen, creeaza_vanzare
from Logic.change_genre import change_genre, title_in_lst


def get_data():
    return [
        creeaza_vanzare(1, 'v1', 'gen1', 60, 'silver'),
        creeaza_vanzare(2, 'v2', 'gen2', 20, 'none'),
        creeaza_vanzare(3, 'v3', 'gen3', 12, 'gold'),
        creeaza_vanzare(4, 'v4', 'gen4', 34, 'silver'),
    ]

def test_change_genre():
    vanzari = get_data()
    vanzari = change_genre(vanzari, 'v1', 'gennou1', [], [])
    vanzari = change_genre(vanzari, 'v2', 'gennou2', [], [])
    assert get_gen(vanzari[0]) == 'gennou1'
    assert get_gen(vanzari[1]) == 'gennou2'
    try:
        _ = change_genre(vanzari, 'v8' , 'gennou8', [], [])
        assert False
    except ValueError:
        assert True  # sau pass

def test_title_in_lst():
    vanzari = get_data()
    assert title_in_lst(vanzari, 'v1') == 1
    assert title_in_lst(vanzari, 'v2') == 2
    assert title_in_lst(vanzari, 'v7') is None

def test_alt_genre():
    test_title_in_lst()
    test_change_genre()
