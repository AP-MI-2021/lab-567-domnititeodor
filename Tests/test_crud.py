from Domain.vanzare import creeaza_vanzare, get_id
from Logic.crud import create, read, update, delete


def get_data():
    return [
        creeaza_vanzare(1, 'v1', 'gen1', 60, 'silver'),
        creeaza_vanzare(2, 'v2', 'gen2', 20, 'none'),
        creeaza_vanzare(3, 'v3', 'gen3', 12, 'gold'),
        creeaza_vanzare(4, 'v4', 'gen4', 34, 'silver'),
    ]


def test_create():
    vanzari = get_data()
    params = (5, 'vnew', 'gen new', 27, 'gold')
    v_new = creeaza_vanzare(*params)
    new_vanzari = create(vanzari, *params)
    assert len(new_vanzari) == len(vanzari) + 1
    assert v_new in new_vanzari


def test_read():
    vanzari = get_data()
    some_v = vanzari[2]
    assert read(vanzari, get_id(some_v)) == some_v
    assert read(vanzari, None) == vanzari


def test_update():
    vanzari = get_data()
    v_updated = creeaza_vanzare(1, 'vnew', 'gen new', 7.2, 'gold')
    updated = update(vanzari, v_updated)
    assert v_updated in updated
    assert v_updated not in vanzari
    assert len(updated) == len(vanzari)


def test_delete():
    vanzari = get_data()
    to_delete = 3
    v_deleted = read(vanzari, to_delete)
    deleted = delete(vanzari, to_delete)
    assert v_deleted not in deleted
    assert v_deleted in vanzari
    assert len(deleted) == len(vanzari) - 1


def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()
