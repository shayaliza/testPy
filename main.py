import os

def create_new_folder(folder_name):
    try:
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")

if __name__ == "__main__":
    folder_name = input("Enter folder name: ")
    create_new_folder(folder_name)
