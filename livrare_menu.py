# livrare_menu.py

from utilities import save_data_to_file

DEFAULT_ERROR_RESPONSE = "Imi pare rau dar nu am inteles actiunea dumneavoastra"

LIVRARE_MENU_TEXT = """
Sub meniu 2. Livrare
1. Statusul livrarii tale.
2. Cat costa livrarea?
3. Vreau sa schimb detaliile livrarii mele.
9. Inapoi
"""

def handle_livrare_menu(from_number, incoming_msg):
    if incoming_msg == "1":
        save_data_to_file('temp_data/awb_search', from_number, incoming_msg)
        return """
Pentru a afla statusul livrarii dvs. va rugam sa ne dati AWB-ul primit prin SMS sau alegeti una din optiunile de mai jos
9. Inapoi
"""
    elif incoming_msg == "2":
        return """
Costul livrarii este de 20,00 lei cu orice firma de curierat din Romania. Optional pe langa taxa de livrare, oferim si Livrare prioritara la doar 7.99 lei extra si Asigurare pe colet la doar 4.99 lei extra
9. Inapoi
"""
    elif incoming_msg == "3":
        return """
Momentan abilitatiile mele nu imi permit sa schimb detaliile comenzii dvs. dar colegii mei din Call Center pot sa va ajute cu drag la numarul de telefon - de Luni pana Vineri intre orele 9:30 - 18:30
9. Inapoi
"""
    elif incoming_msg == "9":
        return "Inapoi"
    else:
        return DEFAULT_ERROR_RESPONSE
