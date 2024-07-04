import os

def create_new_folder(test):
    try:
        os.mkdir(test)
        print(f"Folder '{test}' created successfully.")
    except FileExistsError:
        print(f"Folder '{test}' already exists.")

if __name__ == "__main__":
    # folder_name = input("Enter folder name: ")
    create_new_folder("test")
