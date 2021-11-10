from Domain.vanzare import creeaza_vanzare, get_pret, get_gen
from Logic.apply_discount import apply_discount
from Logic.change_genre import change_genre
from Logic.crud import create, read, update, delete
from Logic.undo_redo import do_undo, do_redo


def test_undo_redo():
    vanzari = []
    undo_list = []
    redo_list = []
    vanzari = create(vanzari, 1, 'Harry Potter', 'Fantasy', 24.99, 'none', undo_list, redo_list)
    vanzari = create(vanzari, 2, 'Shining', 'Horror', 21, 'silver', undo_list, redo_list)
    vanzari = create(vanzari, 3, '1984', 'Dystopian', 21, 'gold', undo_list, redo_list)
    if len(undo_list) > 0:
        vanzari = do_undo(undo_list, redo_list, vanzari)
    assert vanzari[0] == [1, 'Harry Potter', 'Fantasy', 24.99, 'none']
    assert vanzari[1] == [2, 'Shining', 'Horror', 21, 'silver']
    assert read(vanzari, 3) is None
    if len(undo_list) > 0:
        vanzari = do_undo(undo_list, redo_list, vanzari)
    assert vanzari[0] == [1, 'Harry Potter', 'Fantasy', 24.99, 'none']
    assert read(vanzari, 2) is None
    assert read(vanzari, 3) is None
    if len(undo_list) > 0:
        vanzari = do_undo(undo_list, redo_list, vanzari)
    assert read(vanzari, 1) is None
    assert read(vanzari, 2) is None
    assert read(vanzari, 3) is None
    if len(undo_list) > 0:
        vanzari = do_undo(undo_list, redo_list, vanzari)
    assert read(vanzari, 1) is None
    assert read(vanzari, 2) is None
    assert read(vanzari, 3) is None
    vanzari = create(vanzari, 1, 'Harry Potter', 'Fantasy', 24.99, 'none', undo_list, redo_list)
    vanzari = create(vanzari, 2, 'Shining', 'Horror', 21, 'silver', undo_list, redo_list)
    vanzari = create(vanzari, 3, '1984', 'Dystopian', 21, 'gold', undo_list, redo_list)
    if len(redo_list) > 0:
        vanzari = do_redo(undo_list, redo_list, vanzari)
    assert vanzari[0] == [1, 'Harry Potter', 'Fantasy', 24.99, 'none']
    assert vanzari[1] == [2, 'Shining', 'Horror', 21, 'silver']
    assert vanzari[2] == [3, '1984', 'Dystopian', 21, 'gold']
    if len(undo_list) > 0:
        vanzari = do_undo(undo_list, redo_list, vanzari)
    if len(undo_list) > 0:
        vanzari = do_undo(undo_list, redo_list, vanzari)
    if len(redo_list) > 0:
        vanzari = do_redo(undo_list, redo_list, vanzari)
    assert vanzari[0] == [1, 'Harry Potter', 'Fantasy', 24.99, 'none']
    assert vanzari[1] == [2, 'Shining', 'Horror', 21, 'silver']
    assert read(vanzari, 3) is None
    if len(redo_list) > 0:
        vanzari = do_redo(undo_list, redo_list, vanzari)
    assert vanzari[0] == [1, 'Harry Potter', 'Fantasy', 24.99, 'none']
    assert vanzari[1] == [2, 'Shining', 'Horror', 21, 'silver']
    assert vanzari[2] == [3, '1984', 'Dystopian', 21, 'gold']
    if len(undo_list) > 0:
        vanzari = do_undo(undo_list, redo_list, vanzari)
    if len(undo_list) > 0:
        vanzari = do_undo(undo_list, redo_list, vanzari)
    vanzari = create(vanzari, 4, 'Carrie', 'Horror', 24, 'none', undo_list, redo_list)
    if len(redo_list) > 0:
        vanzari = do_redo(undo_list, redo_list, vanzari)
    assert vanzari[0] == [1, 'Harry Potter', 'Fantasy', 24.99, 'none']
    assert vanzari[1] == [4, 'Carrie', 'Horror', 24, 'none']
    if len(undo_list) > 0:
        vanzari = do_undo(undo_list, redo_list, vanzari)
    assert vanzari[0] == [1, 'Harry Potter', 'Fantasy', 24.99, 'none']
    assert read(vanzari, 4) is None
    if len(undo_list) > 0:
        vanzari = do_undo(undo_list, redo_list, vanzari)
    assert read(vanzari, 1) is None
    assert read(vanzari, 4) is None
    if len(redo_list) > 0:
        vanzari = do_redo(undo_list, redo_list, vanzari)
    assert vanzari[0] == [1, 'Harry Potter', 'Fantasy', 24.99, 'none']
    assert read(vanzari, 4) is None
    if len(redo_list) > 0:
        vanzari = do_redo(undo_list, redo_list, vanzari)
    assert vanzari[0] == [1, 'Harry Potter', 'Fantasy', 24.99, 'none']
    assert vanzari[1] == [4, 'Carrie', 'Horror', 24, 'none']
    if len(redo_list) > 0:
        vanzari = do_redo(undo_list, redo_list, vanzari)
    assert vanzari[0] == [1, 'Harry Potter', 'Fantasy', 24.99, 'none']
    assert vanzari[1] == [4, 'Carrie', 'Horror', 24, 'none']


def test_undo_redo_update():
    vanzari = []
    undo_list = []
    redo_list = []
    vanzari = create(vanzari, 1, 'Harry Potter', 'Fantasy', 24.99, 'none', undo_list, redo_list)
    vanzari = create(vanzari, 2, 'Shining', 'Horror', 21, 'silver', undo_list, redo_list)
    vanzari = create(vanzari, 3, '1984', 'Dystopian', 21, 'gold', undo_list, redo_list)
    v_updated = creeaza_vanzare(1, 'vnew', 'gen new', 7.2, 'gold')
    updated = update(vanzari, v_updated, undo_list, redo_list)
    if len(undo_list) > 0:
        updated = do_undo(undo_list, redo_list, updated)
    assert v_updated not in updated
    if len(redo_list) > 0:
        updated = do_redo(undo_list, redo_list, updated)
    assert v_updated in updated


def test_undo_redo_delete():
    vanzari = []
    undo_list = []
    redo_list = []
    vanzari = create(vanzari, 1, 'Harry Potter', 'Fantasy', 24.99, 'none', undo_list, redo_list)
    vanzari = create(vanzari, 2, 'Shining', 'Horror', 21, 'silver', undo_list, redo_list)
    vanzari = create(vanzari, 3, '1984', 'Dystopian', 21, 'gold', undo_list, redo_list)
    to_delete = 3
    v_deleted = read(vanzari, to_delete)
    deleted = delete(vanzari, to_delete, undo_list, redo_list)
    if len(undo_list) > 0:
        deleted = do_undo(undo_list, redo_list, deleted)
    assert v_deleted in deleted
    if len(redo_list) > 0:
        deleted = do_redo(undo_list, redo_list, deleted)
    assert v_deleted not in deleted


def test_undo_redo_discount():
    vanzari = []
    undo_list = []
    redo_list = []
    vanzari = create(vanzari, 1, 'Harry Potter', 'Fantasy', 10, 'none', undo_list, redo_list)
    vanzari = create(vanzari, 2, 'Shining', 'Horror', 10, 'silver', undo_list, redo_list)
    vanzari = create(vanzari, 3, '1984', 'Dystopian', 10, 'gold', undo_list, redo_list)
    vanzari = apply_discount(vanzari, undo_list, redo_list)
    if len(undo_list) > 0:
        vanzari = do_undo(undo_list, redo_list, vanzari)
    assert get_pret(vanzari[0]) == 10
    assert get_pret(vanzari[1]) == 10
    assert get_pret(vanzari[2]) == 10
    if len(redo_list) > 0:
        vanzari = do_redo(undo_list, redo_list, vanzari)
    assert get_pret(vanzari[0]) == 10
    assert get_pret(vanzari[1]) == 9.5
    assert get_pret(vanzari[2]) == 9


def test_undo_redo_genre():
    vanzari = []
    undo_list = []
    redo_list = []
    vanzari = create(vanzari, 1, 'Harry Potter', 'Fantasy', 10, 'none', undo_list, redo_list)
    vanzari = create(vanzari, 2, 'Shining', 'Horror', 10, 'silver', undo_list, redo_list)
    vanzari = create(vanzari, 3, '1984', 'Dystopian', 10, 'gold', undo_list, redo_list)
    vanzari = change_genre(vanzari, '1984', 'SF', undo_list, redo_list)
    if len(undo_list) > 0:
        vanzari = do_undo(undo_list, redo_list, vanzari)
    assert get_gen(vanzari[2]) == 'Dystopian'
    if len(redo_list) > 0:
        vanzari = do_redo(undo_list, redo_list, vanzari)
    assert get_gen(vanzari[2]) == 'SF'


def test_all_undo_redo():
    test_undo_redo()
    test_undo_redo_update()
    test_undo_redo_delete()
    test_undo_redo_discount()
    test_undo_redo_genre()
