import socket
import datetime

# Dirección y puerto del servidor socket
SERVER_ADDRESS = ('localhost', 23456)

def log_activity(message):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'[{timestamp}] {message}')

# Función para convertir texto de minúsculas a MAYÚSCULAS
def convert_to_uppercase(text):
    return text.upper()

# Función para realizar la suma de dos números
def sum_two_numbers(num1, num2):
    try:
        result = int(num1) + int(num2)
        return f"La suma de {num1} y {num2} es: {result}"
    except ValueError:
        return "Error: Por favor ingrese números válidos."

# Función para manejar las opciones del menú
def handle_menu_option(option):
    if option == '1':
        return "MAYÚSCULAS: "
    elif option == '2':
        return "SUMA"
    elif option == '3':
        return "Mostrando la fecha y hora actual..."
    elif option == '4':
        return "Saliendo del programa..."
    else:
        return "Opción no válida."

# Crear un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket a la dirección y puerto del servidor socket
server_socket.bind(SERVER_ADDRESS)

# Escuchar por conexiones entrantes
server_socket.listen(1)

log_activity("Servidor iniciado. Esperando conexiones entrantes...")

while True:
    # Esperar una conexión
    connection, client_address = server_socket.accept()

    try:
        log_activity(f"Conexión establecida desde {client_address}")

        # Menú de opciones
        while True:
            # Recibir la opción del cliente
            option = connection.recv(1024).decode().strip()

            if not option:
                break

            if option == '4':
                log_activity("Cliente seleccionó salir del programa.")
                connection.sendall(handle_menu_option(option).encode())
                break

            response = handle_menu_option(option)

            if option == '1':
                # Si la opción es convertir texto a MAYÚSCULAS
                connection.sendall(response.encode())
                text = connection.recv(1024).decode().strip()
                converted_text = convert_to_uppercase(text)
                connection.sendall(converted_text.encode())
            elif option == '2':
                # Si la opción es realizar la suma de dos números
                connection.sendall(response.encode())
                num1 = connection.recv(1024).decode().strip()
                num2 = connection.recv(1024).decode().strip()  # Aquí debería ser solo una vez
                result = sum_two_numbers(num1, num2)
                connection.sendall(result.encode())
            elif option == '3':
                # Si la opción es mostrar la fecha y hora actual
                connection.sendall(response.encode())
                current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                connection.sendall(current_datetime.encode())
            else:
                # Si la opción no es válida
                connection.sendall(response.encode())

    except ConnectionResetError:
        log_activity("Conexión cerrada por el cliente.")
        break

    finally:
        # Cerrar la conexión
        connection.close()
