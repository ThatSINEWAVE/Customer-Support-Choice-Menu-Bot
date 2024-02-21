# main_menu.py

DEFAULT_ERROR_RESPONSE = "Imi pare rau dar nu am inteles actiunea dumneavoastra"

MAIN_MENU_TEXT = """
Buna ziua, alegeti din meniul de mai jos din ce motiv ne contactati:
1. Comenzi
2. Livrare
3. Returnari
4. Feedback
5. Informatii generale
9. STOP
"""

def handle_main_menu(from_number, incoming_msg):
    if incoming_msg == "1":
        return COMENZI_MENU_TEXT
    elif incoming_msg == "2":
        return LIVRARE_MENU_TEXT
    elif incoming_msg == "3":
        return RETURNARI_MENU_TEXT
    elif incoming_msg == "4":
        return FEEDBACK_MENU_TEXT
    elif incoming_msg == "5":
        return INFORMATII_GENERALE_MENU_TEXT
    elif incoming_msg == "9":
        return "Conversatie incheiata. Multumim!"
    else:
        return DEFAULT_ERROR_RESPONSE
