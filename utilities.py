import os


def save_data_to_file(folder_name, file_name, data):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    with open(os.path.join(folder_name, f"{file_name}.txt"), 'w') as file:
        file.write(data)
