import pickle
from tkinter import *
from tkinter import ttk
from time import sleep

ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_EXIT = 5

SAVE_FILE_NAME = "contacts.save"

MENU_OPTIONS = [ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_FIND_CONTACT, ACTION_EXPORT_CONTACT, ACTION_EXIT]


def ask_until_option_expected(options):
    selected_action = ""

    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action) not in options):
        selected_action = input("¿Qué opción deseas? ")

    return int(selected_action)


def show_menu():
    print("Acciones disponinbles: ")
    print("1 - Añadir contacto")
    print("2 - Eliminar contacto")
    print("3 - Buscar un contacto")
    print("4 - Exportar contactos a un CSV")
    print("5 - Salir")
    return ask_until_option_expected(MENU_OPTIONS)


def add_contact(contacts, name, phone, email):

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    return contact


def ask_new_contact(contacts):
    print("\n\nAñadir contacto\n")
    contact = add_contact(contacts, input("Nombre: "), input("Teléfono: "), input("Email: "))
    print("Se ha añadido el contacto {} correctamente\n".format(contact["name"]))
    sleep(2)


def tk_display_contacts_ui(contacts, name, phone, email, show_list_frame):
    contact = add_contact(contacts, name, phone, email)
    cols, row = show_list_frame.grid_size()
    ttk.Label(show_list_frame, text=contact["name"]).grid(column=1, row=row)
    ttk.Label(show_list_frame, text=contact["phone"]).grid(column=2, row=row)
    ttk.Label(show_list_frame, text=contact["email"]).grid(column=3, row=row)


def remove_contact(contacts):
    print("\n\nEliminar contacto\n")
    search_term = input("Introducir el nombre del contacto o parte de él: ")
    found_contacts = []

    print("He encontrado los siguientes contactos:")
    contact_indexes = []
    contact_counter = 0

    for contact in contacts:
        if contact["name"].find(search_term) >= 0:
            found_contacts.append(contact)
            print("{} - {}".format(contact_counter, contact["name"]))
            contact_indexes.append(contact_counter)
            contact_counter += 1

    contact_index = 0

    if len(contact_indexes) > 1:
        contact_index = ask_until_option_expected(contact_indexes)

    elif len(contact_indexes) == 0:
        print("No se ha encontrado ninguno.")
        return

    print('Seguro que quieres borrar a {}'.format(found_contacts[contact_index]["name"]))
    print('Si = 1')
    print('No = 2')
    if ask_until_option_expected([1, 2]) == 1:
        pass
    else:
        return

    print("\nSe ha eliminado {} de tu lista\n".format(found_contacts[contact_index]["name"]))
    contact_for_remove = contacts.index(found_contacts[contact_index])
    contacts.pop(contact_for_remove)
    sleep(2)


def find_contact(contacts):
    print("\n\nBuscar contacto\n")
    search_term = input("Introducir el nombre del contacto o parte de él: ")
    found_contacts = []

    print("He encontrado los siguientes contactos:")
    contact_indexes = []
    contact_counter = 0

    for contact in contacts:
        if contact["name"].find(search_term) >= 0:
            found_contacts.append(contact)
            print("{} - {}".format(contact_counter, contact["name"]))
            contact_indexes.append(contact_counter)
            contact_counter += 1

    contact_index = 0

    if len(contact_indexes) > 1:
        contact_index = ask_until_option_expected(contact_indexes)
    elif len(contact_indexes) == 0:
        print("No se ha encontrado ninguno.")
        return

    print("\nInformación sobre {}\n".format(found_contacts[contact_index]["name"]))
    print("Nombre: {name}, Telefono: {phone}, Email: {email}\n\n".format(**found_contacts[contact_index]))
    sleep(2)


def export_contacts():

    pass


def load_contacts():
    try:
        return pickle.load(open(SAVE_FILE_NAME, "rb"))
    except FileNotFoundError:
        return []


def tk_load_contacts_ui(contacts, show_list_frame):
    for contact in contacts:
        cols, row = show_list_frame.grid_size()
        ttk.Label(show_list_frame, text=contact["name"]).grid(column=1, row=row)
        ttk.Label(show_list_frame, text=contact["phone"]).grid(column=2, row=row)
        ttk.Label(show_list_frame, text=contact["email"]).grid(column=3, row=row)


def save_contacts(contacts):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)
    print("Datos guardados correctamente.")


def main():
    contacts = load_contacts()

    root = Tk()
    root.title("Agenda")

    add_frame = ttk.Frame(root, padding="30 12 30 12")
    add_frame.grid()

    show_list_frame = ttk.Frame(root, padding="30 12 30 12")
    show_list_frame.grid()

    name = StringVar()
    phone = StringVar()
    email = StringVar()

    ttk.Label(add_frame, text="Nombre").grid(column=1, row=1, sticky=W)
    ttk.Label(add_frame, text="Numero").grid(column=2, row=1, sticky=W)
    ttk.Label(add_frame, text="Email").grid(column=3, row=1, sticky=W)

    ttk.Entry(add_frame, width=12, textvariable=name).grid(column=1, row=2)
    ttk.Entry(add_frame, width=12, textvariable=phone).grid(column=2, row=2)
    ttk.Entry(add_frame, width=30, textvariable=email).grid(column=3, row=2)

    ttk.Button(add_frame,
               text="Añadir",
               command=lambda: tk_display_contacts_ui(contacts, name.get(), phone.get(), email.get(), show_list_frame)
               ).grid(column=3, row=3, sticky=E)

    ttk.Label(show_list_frame, text="Nombre").grid(column=1, row=1, sticky=W)
    ttk.Label(show_list_frame, text="Numero").grid(column=2, row=1, sticky=W)
    ttk.Label(show_list_frame, text="Email").grid(column=3, row=1)

    for child in add_frame.winfo_children():
        child.grid_configure(padx=3, pady=3)

    for child in show_list_frame.winfo_children():
        child.grid_configure(padx=8, pady=8)

    tk_load_contacts_ui(contacts, show_list_frame)

    mainloop()
    save_contacts(contacts)


if __name__ == "__main__":
    main()
