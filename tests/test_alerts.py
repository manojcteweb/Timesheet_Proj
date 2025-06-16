import pytest
from unittest.mock import MagicMock
from services.alert_service import AlertService
from services.database_service import DatabaseService

@pytest.fixture
def alert_service():
    service = AlertService()
    service.notification_service.send_notification = MagicMock()
    service.database_service.log_alert = MagicMock()
    return service

@pytest.fixture
def database_service():
    service = DatabaseService(db_uri='mongodb://localhost:27017/', db_name='alert_db')
    service.alerts_collection.insert_one = MagicMock()
    service.alerts_collection.find = MagicMock(return_value=[])
    return service


def test_generate_alert(alert_service):
    message = "Test alert message"
    alert_service.generate_alert(message)
    
    # Check if send_notification was called
    alert_service.notification_service.send_notification.assert_called_once_with(message)
    
    # Check if log_alert was called
    alert_service.database_service.log_alert.assert_called_once_with(message)


def test_send_alert(alert_service):
    message = "Test alert message"
    alert_service.send_alert(message)
    
    # Check if send_notification was called
    alert_service.notification_service.send_notification.assert_called_once_with(message)
    
    # Check if log_alert was called
    alert_service.database_service.log_alert.assert_called_once_with(message)


def test_log_alert(database_service):
    message = "Test alert message"
    database_service.log_alert(message)
    
    # Check if insert_one was called
    database_service.alerts_collection.insert_one.assert_called_once_with({'message': message})


def test_retrieve_alerts(database_service):
    alerts = database_service.retrieve_alerts()
    
    # Check if find was called
    database_service.alerts_collection.find.assert_called_once()
    
    # Check if the returned alerts list is empty
    assert alerts == []