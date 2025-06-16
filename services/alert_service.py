import logging
from services.notification_service import NotificationService
from services.database_service import DatabaseService

class AlertService:
    def __init__(self):
        self.logger = logging.getLogger('AlertService')
        self.notification_service = NotificationService()
        self.database_service = DatabaseService(db_uri='mongodb://localhost:27017/', db_name='alert_db')

    def generate_alert(self, message: str):
        self.logger.info(f"Generating alert: {message}")
        # Here you can add logic to format or process the alert message
        self.send_alert(message)

    def send_alert(self, message: str):
        self.logger.info(f"Sending alert: {message}")
        try:
            # Send the alert using the notification service
            self.notification_service.send_notification(message)
            # Log the alert in the database
            self.database_service.log_alert(message)
        except Exception as e:
            self.logger.error(f"An error occurred while sending alert: {str(e)}")