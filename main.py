# import os

# def create_new_folder(folder_name):
#     try:
#         os.mkdir(folder_name)
#         print(f"Folder '{folder_name}' created successfully.")
#     except FileExistsError:
#         print(f"Folder '{folder_name}' already exists.")

# if __name__ == "__main__":
#     create_new_folder("test")


import os

def create_new_folder(base_folder):
    # Check if 'test' folder exists
    if os.path.exists(base_folder):
        # If 'test' folder exists, create 'test1'
        new_folder = base_folder + "1"
        try:
            os.mkdir(new_folder)
            print(f"Folder '{new_folder}' created successfully.")
        except FileExistsError:
            print(f"Folder '{new_folder}' already exists.")
    else:
        # If 'test' folder does not exist, create 'test'
        try:
            os.mkdir(base_folder)
            print(f"Folder '{base_folder}' created successfully.")
        except FileExistsError:
            print(f"Folder '{base_folder}' already exists.")

if __name__ == "__main__":
    base_folder = "test"
    create_new_folder(base_folder)
