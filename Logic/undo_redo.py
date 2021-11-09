def do_undo(undo_list: list, redo_list: list, current_list: list):
    """
    Aplica o actiune de tip "undo" listei de vanzari
    :param undo_list: o lista care memoreaza lista de vanzari inainte de modificari
    :param redo_list: o lista care memoreaza lista de vanzari dupa modificari
    :param current_list: lista de vanzari curenta
    :return: lista inainte de ultima modificare
    """
    if undo_list:
        top_undo = undo_list.pop()
        redo_list.append(current_list)
        return top_undo

    return None


def do_redo(undo_list: list, redo_list: list, current_list: list):
    """
    Aplica o actiune de tip "redo" listei de vanzari
    :param undo_list: o lista care memoreaza lista de vanzari inainte de modificari
    :param redo_list: o lista care memoreaza lista de vanzari dupa modificari
    :param current_list: lista de vanzari curenta
    :return: lista dupa ultima modificare
    """
    if redo_list:
        top_redo = redo_list.pop()
        undo_list.append(current_list)
        return top_redo

    return None
