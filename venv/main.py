import PySimpleGUI as sg
from password_manager import generate_key, encrypt_password, decrypt_password
from data import CATEGORIES

def main():
    sg.theme("LightGrey1")

    layout = [
        [sg.Text("Введіть пароль: "), sg.InputText(key='password')],
        [sg.Button("Зашифрувати"), sg.Button("Розшифрувати")],
        [sg.Text("", size=(30, 1), key='output')],
    ]

    window = sg.Window("Менеджер паролів", layout, resizable=True)

    key = generate_key()  # Генеруємо ключ один раз при старті програми

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        elif event == 'Зашифрувати':
            user_password = values['password']
            if user_password:
                encrypted_password = encrypt_password(key, user_password)
                window['output'].update(f"Зашифрований пароль: {encrypted_password}")

        elif event == 'Розшифрувати':
            encrypted_password = values['password']
            if encrypted_password:
                decrypted_password = decrypt_password(key, encrypted_password)
                window['output'].update(f"Розшифрований пароль: {decrypted_password}")

    window.close()

if __name__ == "__main__":
    main()
