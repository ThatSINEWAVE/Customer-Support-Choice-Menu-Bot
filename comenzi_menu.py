# comenzi_menu.py

from utilities import save_data_to_file

DEFAULT_ERROR_RESPONSE = "Imi pare rau dar nu am inteles actiunea dumneavoastra"

COMENZI_MENU_TEXT = """
Sub meniu 1. Comenzi
1. Plasarea unei comenzi
2. Informatii despre comanda plasata
3. Detalii despre produsele comandate
4. Confirmati detaliile comenzii tale
9. Inapoi
"""

def handle_comenzi_menu(from_number, incoming_msg):
    if incoming_msg == "1":
        return """
Pentru a plasa o comanda, puteti naviga pe site-ul nostru si sa efectuati comanda chiar pe site sau puteti sa ne contactati telefonic la numarul - unde unul din operatorii nostri va vor ajuta sa plasati o comanda cu produsele dorite!
9. Inapoi
"""
    elif incoming_msg == "2":
        save_data_to_file('temp_data/order_info', from_number, incoming_msg)
        return """
Pentru a afla informatii despre comanda dvs. va rugam sa ne trimiteti numarul comenzii, acesta poate fi gasit pe email-ul trimis automat in momentul in care ati plasat comanda
9. Inapoi
"""
    # ... Handle other options ...

    else:
        return DEFAULT_ERROR_RESPONSE
