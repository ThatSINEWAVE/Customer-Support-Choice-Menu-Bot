# informatii_generale_menu.py

from utilities import save_data_to_file

DEFAULT_ERROR_RESPONSE = "Imi pare rau dar nu am inteles actiunea dumneavoastra"

INFORMATII_GENERALE_MENU_TEXT = """
Sub meniu 5. Informatii Generale
1. Detalii despre produse.
2. Contact
3. Despre noi
9. Inapoi
"""


def handle_informatii_generale_menu(from_number, incoming_msg):
    if incoming_msg == "1":
        save_data_to_file('temp_data/product_info', from_number, incoming_msg)
        return """
Va rugam lasati numele sau link-ul produsului despre care doriti sa aflati mai multe detalii
9. Inapoi
"""
    elif incoming_msg == "2":
        return """
Daca doriti sa intrati in contact cu echipa noastra puteti sa ne apelati gratuit la numarul de telefon - oricand de Luni pana Vineri intre orele 9:30 - 18:30, la adresa de email oricare.ro@gmail.com sau la formularul de contact de mai jos
LINK HERE
9. Inapoi
"""
    elif incoming_msg == "3":
        return """
Suntem o echipă pasionată de descoperirea și împărtășirea celor mai bune resurse și informații pentru a vă ajuta să luați cele mai bune decizii în diverse aspecte ale vieții voastre. Cu o experiență vastă în domenii variate, precum tehnologie, călătorii, sănătate, educație și multe altele, ne-am propus să vă aducem articole și ghiduri relevante și actualizate pentru a vă sprijini în fiecare pas al călătoriei voastre.
La LINK HERE, credem în puterea cunoașterii și în facilitarea accesului la informații utile și de încredere. Ne străduim să oferim conținut de calitate, verificat și bine documentat, astfel încât să puteți lua decizii informate și să vă îmbunătățiți calitatea vieții. Fie că sunteți în căutarea celor mai recente știri, sfaturi practice sau ghiduri detaliate, suntem aici pentru a vă ghida în fiecare etapă.
În plus, suntem dedicați interacțiunii cu comunitatea noastră. Ne bucurăm să primim feedback-ul vostru și să răspundem întrebărilor voastre. Vă invităm să navigați pe site-ul nostru și să explorați conținutul bogat pe care l-am pregătit pentru voi.
9. Inapoi
"""
    elif incoming_msg == "9":
        return "Inapoi"
    else:
        return DEFAULT_ERROR_RESPONSE
