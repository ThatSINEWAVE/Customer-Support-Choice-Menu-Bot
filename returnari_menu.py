# returnari_menu.py

from utilities import save_data_to_file

DEFAULT_ERROR_RESPONSE = "Imi pare rau dar nu am inteles actiunea dumneavoastra"

RETURNARI_MENU_TEXT = """
Sub meniu 3. Returnari
1. Vreau sa fac un retur.
2. Care este statusul returnarii mele?
3. Vreau sa primesc banii inapoi.
9. Inapoi
"""

def handle_returnari_menu(from_number, incoming_msg):
    if incoming_msg == "1":
        save_data_to_file('temp_data/return_list', from_number, incoming_msg)
        return """
Pentru a identifica comanda dumneavoastra va rugam sa ne dati numarul de comanda primit prin email
9. Inapoi
"""
    elif incoming_msg == "2":
        save_data_to_file('temp_data/active_returns', from_number, incoming_msg)
        return """
Pentru a putea verifica statusul returului dumneavoastra va rugam sa ne dati numarul de comanda primit prin email.
9. Inapoi
"""
    # ... Handle other options ...

    else:
        return DEFAULT_ERROR_RESPONSE
