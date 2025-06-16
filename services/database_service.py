import logging
from pymongo import MongoClient

class DatabaseService:
    def __init__(self, db_uri: str, db_name: str):
        self.logger = logging.getLogger('DatabaseService')
        self.client = MongoClient(db_uri)
        self.db = self.client[db_name]
        self.alerts_collection = self.db['alerts']

    def log_alert(self, message: str):
        self.logger.info(f"Logging alert to database: {message}")
        try:
            alert_record = {'message': message}
            self.alerts_collection.insert_one(alert_record)
            self.logger.info("Alert logged successfully.")
        except Exception as e:
            self.logger.error(f"An error occurred while logging alert: {str(e)}")

    def retrieve_alerts(self):
        self.logger.info("Retrieving alerts from database.")
        try:
            alerts = list(self.alerts_collection.find())
            self.logger.info(f"Retrieved {len(alerts)} alerts.")
            return alerts
        except Exception as e:
            self.logger.error(f"An error occurred while retrieving alerts: {str(e)}")
            return []