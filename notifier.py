import os
import smtplib
from abc import ABC, abstractmethod
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate, make_msgid
from dotenv import load_dotenv

# Carga variables de entorno locales desde el archivo .env
load_dotenv()


# -------------------------------------------------------------------------
# Concepto Semana 1: Interfaz / Clase Abstracta (Contrato base común)
# Define la firma del método enviar() que todas las clases deben implementar.
# -------------------------------------------------------------------------
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje: str, destinatario: str = "") -> None:
        pass


# -------------------------------------------------------------------------
# Entregable 1 (Semana 3): Identificar e implementar clases concretas
# Principio de Responsabilidad Única (SRP): Cada clase maneja su propio canal.
# -------------------------------------------------------------------------
class NotificadorEmail(Notificador):
    def enviar(self, mensaje: str, destinatario: str = "") -> None:
        if not destinatario:
            raise ValueError("El correo electrónico requiere un destinatario válido.")

        remitente = os.getenv("EMAIL_USER")
        password = os.getenv("EMAIL_PASS")

        if not remitente or not password:
            raise ValueError("Credenciales SMTP no configuradas en el archivo .env")

        # Construcción de encabezados estándar RFC 2822 para evitar filtros de spam
        msg = MIMEMultipart()
        msg["From"] = remitente
        msg["To"] = destinatario
        msg["Date"] = formatdate(localtime=True)
        msg["Message-ID"] = make_msgid()
        msg["Subject"] = "Notificación del Sistema (Demo Factory Method)"
        msg.attach(MIMEText(mensaje, "plain", "utf-8"))

        # Conexión segura con servidor SMTP (Gmail SSL - Puerto 465)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
            servidor.login(remitente, password)
            servidor.send_message(msg)

        print(f"[EMAIL REAL] Correo enviado exitosamente a: {destinatario}")


class NotificadorSMS(Notificador):
    def enviar(self, mensaje: str, destinatario: str = "") -> None:
        print(f"[SMS SIMULADO] Enviando SMS a {destinatario or 'usuario'}: {mensaje}")


# Criterio de evaluación: Extensión con bajo impacto (WhatsApp)
class NotificadorWhatsApp(Notificador):
    def enviar(self, mensaje: str, destinatario: str = "") -> None:
        print(f"[WHATSAPP SIMULADO] Enviando mensaje a {destinatario or 'usuario'}: {mensaje}")