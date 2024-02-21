# main_driver.py

from comenzi_menu import handle_comenzi_menu
from livrare_menu import handle_livrare_menu
from returnari_menu import handle_returnari_menu
from feedback_menu import handle_feedback_menu
from informatii_generale_menu import handle_informatii_generale_menu

MAIN_MENU_TEXT = """
Meniul Principal:
Buna ziua, alegeti din meniul de mai jos din ce motiv ne contactati:
1. Comenzi
2. Livrare
3. Returnari
4. Feedback
5. Informatii generale
9. STOP
"""


def main():
    current_menu = "main"
    while True:
        if current_menu == "main":
            user_input = input(MAIN_MENU_TEXT)
            if user_input == "1":
                current_menu = "comenzi"

            elif user_input == "2":
                current_menu = "livrare"

            elif user_input == "3":
                current_menu = "returnari"

            elif user_input == "4":
                current_menu = "feedback"

            elif user_input == "5":
                current_menu = "informatii_generale"

            elif user_input == "9":
                print("Goodbye!")
                break
            else:
                print("Imi pare rau dar nu am inteles actiunea dumneavoastra")

        elif current_menu == "comenzi":
            user_input = input(handle_comenzi_menu())
            if user_input == "9":
                current_menu = "main"

        elif current_menu == "livrare":
            user_input = input(handle_livrare_menu())
            if user_input == "9":
                current_menu = "main"

        elif current_menu == "returnari":
            user_input = input(handle_returnari_menu())
            if user_input == "9":
                current_menu = "main"

        elif current_menu == "feedback":
            user_input = input(handle_feedback_menu())
            if user_input == "9":
                current_menu = "main"

        elif current_menu == "informatii_generale":
            user_input = input(handle_informatii_generale_menu())
            if user_input == "9":
                current_menu = "main"

        else:
            # In case of any unexpected state, reset to main menu
            print("Oops, something went wrong. Returning to main menu.")
            current_menu = "main"


if __name__ == "__main__":
    main()
