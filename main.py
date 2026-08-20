from factory import NotificadorFactory

def main() -> None:
    print("=================================================")
    print("   SISTEMA DE NOTIFICACIONES (ENTORNO CERRADO)")
    print("=================================================")
    print("Canales: email (real), sms (simulado), whatsapp (simulado)")
    print("Escribe 'salir' para terminar.\n")

    while True:
        canal = input("Ingrese el canal deseado: ").strip()

        if canal.lower() == "salir":
            print("\nCerrando sistema.")
            break

        if not canal:
            continue

        destinatario = ""
        if canal.lower() == "email":
            destinatario = input("Ingrese el correo destino (ej. tu_correo@gmail.com): ").strip()

        mensaje = input(f"Ingrese el mensaje para [{canal}]: ").strip()

        try:
            notificador = NotificadorFactory.crear_notificador(canal)
            notificador.enviar(mensaje, destinatario)
            print(">> Operación completada.\n")
        except Exception as error:
            print(f"[ERROR]: {error}\n")

if __name__ == "__main__":
    main()