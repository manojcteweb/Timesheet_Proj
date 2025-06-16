import logging

class NotificationService:
    def __init__(self):
        self.logger = logging.getLogger('NotificationService')
        self.channels = []

    def configure_channels(self, channels: list):
        self.logger.info(f"Configuring channels: {channels}")
        self.channels = channels

    def send_notification(self, message: str):
        self.logger.info(f"Sending notification: {message}")
        for channel in self.channels:
            self.logger.info(f"Sending to channel: {channel}")
            # Here you would implement the logic to send a notification to each channel
            # For example, sending an email or a message to a messaging service
            pass
