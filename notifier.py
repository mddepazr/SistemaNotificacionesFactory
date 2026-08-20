import os
import smtplib
from abc import ABC, abstractmethod
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate, make_msgid
from dotenv import load_dotenv

load_dotenv()  # Carga las credenciales del archivo .env


class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje: str, destinatario: str = "") -> None:
        pass


class NotificadorEmail(Notificador):
    def enviar(self, mensaje: str, destinatario: str = "") -> None:
        if not destinatario:
            raise ValueError("El correo electrónico requiere un destinatario válido.")

        remitente = os.getenv("EMAIL_USER")
        password = os.getenv("EMAIL_PASS")

        if not remitente or not password:
            raise ValueError("Credenciales de correo no configuradas en el archivo .env")

        msg = MIMEMultipart()
        msg["From"] = remitente
        msg["To"] = destinatario
        msg["Date"] = formatdate(localtime=True)
        msg["Message-ID"] = make_msgid()
        msg["Subject"] = "TE AMOOO"
        msg.attach(MIMEText(mensaje, "plain", "utf-8"))

        # Conexión segura con el servidor SMTP de Gmail (Puerto 465 SSL)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
            servidor.login(remitente, password)
            servidor.send_message(msg)

        print(f"[EMAIL REAL] Correo enviado exitosamente a: {destinatario}")


class NotificadorSMS(Notificador):
    def enviar(self, mensaje: str, destinatario: str = "") -> None:
        print(f"[SMS SIMULADO] Enviando SMS a {destinatario or 'usuario'}: {mensaje}")


class NotificadorWhatsApp(Notificador):
    def enviar(self, mensaje: str, destinatario: str = "") -> None:
        print(f"[WHATSAPP SIMULADO] Enviando mensaje a {destinatario or 'usuario'}: {mensaje}")