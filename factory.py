from notifier import Notificador, NotificadorEmail, NotificadorSMS, NotificadorWhatsApp


# -------------------------------------------------------------------------
# Entregable 2 (Semana 3): Fábrica (Factory Method)
# Centraliza y encapsula la instanciación de objetos.
# Cumple con el Principio Abierto/Cerrado (OCP): evita condicionales dispersos.
# -------------------------------------------------------------------------
class NotificadorFactory:
    @staticmethod
    def crear_notificador(tipo: str) -> Notificador:
        tipo_normalizado = tipo.strip().lower()

        if tipo_normalizado == "email":
            return NotificadorEmail()
        elif tipo_normalizado == "sms":
            return NotificadorSMS()
        elif tipo_normalizado == "whatsapp":
            return NotificadorWhatsApp()
        else:
            raise ValueError(f"Tipo de notificador no válido: {tipo}")