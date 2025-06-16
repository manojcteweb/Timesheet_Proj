import logging
from fastapi import APIRouter, HTTPException
from services.alert_service import AlertService
from services.database_service import DatabaseService

router = APIRouter()

class AlertController:
    def __init__(self):
        self.logger = logging.getLogger('AlertController')
        self.alert_service = AlertService()
        self.database_service = DatabaseService(db_uri='mongodb://localhost:27017/', db_name='alert_db')

    def set_alert_rules(self, rules: dict):
        self.logger.info(f"Setting alert rules: {rules}")
        try:
            # Here you would implement the logic to set alert rules
            # For example, storing them in a database or a configuration file
            pass
        except Exception as e:
            self.logger.error(f"An error occurred while setting alert rules: {str(e)}")
            raise HTTPException(status_code=500, detail="Failed to set alert rules.")

    def get_alerts(self):
        self.logger.info("Fetching alerts.")
        try:
            alerts = self.database_service.retrieve_alerts()
            return alerts
        except Exception as e:
            self.logger.error(f"An error occurred while fetching alerts: {str(e)}")
            raise HTTPException(status_code=500, detail="Failed to fetch alerts.")

# FastAPI route definitions
@router.post("/alerts/rules")
async def set_alert_rules(rules: dict):
    controller = AlertController()
    controller.set_alert_rules(rules)
    return {"message": "Alert rules set successfully."}

@router.get("/alerts")
async def get_alerts():
    controller = AlertController()
    return controller.get_alerts()