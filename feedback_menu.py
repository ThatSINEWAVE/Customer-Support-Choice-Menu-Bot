# feedback_menu.py

from utilities import save_data_to_file

DEFAULT_ERROR_RESPONSE = "Imi pare rau dar nu am inteles actiunea dumneavoastra"

FEEDBACK_MENU_TEXT = """
Sub meniu 4. Feedback
1. Scrie o recenzie despre un produs.
2. Ai intampinat probleme cu operatorii nostri?
3. Spune opinia ta.
4. Raporteaza o problema cu site-ul.
9. Inapoi
"""

def handle_feedback_menu(from_number, incoming_msg):
    if incoming_msg == "1":
        save_data_to_file('temp_data/customer_reviews', from_number, incoming_msg)
        return """
Va rugam scrieti numele produsului si recenzia dumneavoasta. Ne bucuram ca ne ajutati sa ne imbunatatim calitatea serviciilor oferite!
9. Inapoi
"""
    elif incoming_msg == "2":
        save_data_to_file('temp_data/callcenter_issues', from_number, incoming_msg)
        return """
In cazul in care ati intampinat probleme cu unul din operatorii nostri din Call Center va rugam sa ne lasati numele operatorului in cazul in care il aveti si sa ne spuneti in ce data sa intamplat apelul.
Ne bucuram ca ne ajutati sa ne imbunatatim calitatea serviciilor oferite!
9. Inapoi
"""
    # ... Handle other options ...

    else:
        return DEFAULT_ERROR_RESPONSE
