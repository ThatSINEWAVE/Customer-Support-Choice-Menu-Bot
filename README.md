# Choice Menu Chatbot Application

## Overview
Choice Menu Chatbot is a text-based interactive application designed to facilitate various customer interactions, including order management, delivery inquiries, returns handling, providing feedback, and offering general information about products and services.

## Application Structure
The application is structured into multiple Python modules, each serving a specific function within the overall system. The key modules include:

- `main.py`: The entry point of the application, initiating the chatbot interface.
- `main_driver.py`: Contains the core logic for navigating through the main and submenus based on user input.
- `main_menu.py`: Manages the main menu of the application, offering users the initial set of options.
- Submenu Handlers:
  - `comenzi_menu.py`: Handles order-related queries and actions.
  - `livrare_menu.py`: Manages delivery-related inquiries.
  - `returnari_menu.py`: Deals with return requests and status checks.
  - `feedback_menu.py`: Collects user feedback on products and services.
  - `informatii_generale_menu.py`: Provides general information about the company and its offerings.
- `config.py`: Stores configuration settings, including directory paths for data storage.
- `credentials.py`: Contains sensitive credentials, such as Twilio API keys, for external services.
- `utilities.py`: Provides utility functions, such as `save_data_to_file`, used across various modules for data handling.

## Features
- **User Interaction**: Through a text-based menu system, users can navigate various services offered by the chatbot.
- **Data Handling**: User inputs and system-generated data are organized and stored efficiently, allowing for easy access and management.
- **Modular Design**: Each component of the application is contained within its own module, promoting modularity and ease of maintenance.

## ☕ [Support my work on Ko-Fi](https://ko-fi.com/thatsinewave)

## Getting Started
1. Clone the repository to your local machine.
2. Ensure Python 3.x is installed.
3. Install required dependencies (if any)
4. Run `python main.py` to start the chatbot.
5. Follow the on-screen instructions to interact with the chatbot.

## Dependencies
- Twilio API (for messaging capabilities)
- Python Standard Library modules like `os`

## Disclaimer
The Choice Menu Chatbot is primarily designed for handling customer support cases for an online store. Please note that the bot's responses and interaction details are primarily in Romanian. This design choice caters to our target user base and ensures a more natural and accessible communication experience for our Romanian-speaking customers.


## Contributing
Contributions to the Choice Menu Chatbot are welcome!

## License
This project is open-sourced under the MIT License.
