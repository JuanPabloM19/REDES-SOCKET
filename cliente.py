import socket

# Dirección y puerto del servidor socket
SERVER_ADDRESS = ('localhost', 23456)

def main():
    # Crear un socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conectar el socket al servidor socket
        client_socket.connect(SERVER_ADDRESS)

        while True:
            # Mostrar el menú
            print("\nHola, bienvenido.\n")
            print("Puedes realizar las siguientes opciones:\n")
            print("1- Pasar de minúscula a MAYÚSCULA")
            print("2- Realizar una suma de dos números")
            print("3- Mostrar la fecha y hora actual")
            print("4- Salir y cerrar el cliente\n")

            # Solicitar al usuario que seleccione una opción
            option = input("Seleccione una opción: ")

            # Enviar la opción al servidor
            client_socket.sendall(option.encode())

            # Recibir y procesar la respuesta del servidor
            response = client_socket.recv(1024).decode()

            if option == '1':
                # Si la opción es convertir texto a MAYÚSCULAS
                print(response)
                text = input("Ingrese el texto a convertir a MAYÚSCULAS: ")
                client_socket.sendall(text.encode())
                converted_text = client_socket.recv(1024).decode()
                print("Texto convertido a MAYÚSCULAS:", converted_text)
            elif option == '2':
                # Si la opción es realizar la suma de dos números
                print(response)
                num1 = input("Ingrese el primer número: ")
                num2 = input("Ingrese el segundo número: ")
                client_socket.sendall(num1.encode())
                client_socket.sendall(num2.encode())
                
                # Recibir el resultado de la suma del servidor
                result = client_socket.recv(1024).decode()
                print("Resultado de la suma:", result)
            elif option == '3':
                # Si la opción es mostrar la fecha y hora actual
                print(response)
                current_datetime = client_socket.recv(1024).decode()
                print("Fecha y hora actual:", current_datetime)
            elif option == '4':
                # Si la opción es salir
                print(response)
                break
            else:
                print(response)

    except Exception as e:
        print("Ocurrió un error:", e)

    finally:
        # Cerrar el socket
        client_socket.close()

if __name__ == "__main__":
    main()
