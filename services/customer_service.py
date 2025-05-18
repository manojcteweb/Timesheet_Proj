import logging
from fastapi import HTTPException
from models.customer_model import Customer
from schemas.customer_schema import CustomerCreate, CustomerUpdate
from database.customer_db import customers_collection
from logging.audit_log import log_action
from security.auth import verify_token

logger = logging.getLogger(__name__)

class CustomerService:
    @staticmethod
    def create_customer(customer_data: CustomerCreate) -> Customer:
        CustomerService._validate_customer_data(customer_data)
        CustomerService._authorize_request()
        customer = CustomerService._create_customer_in_db(customer_data)
        CustomerService._log_creation(customer)
        return customer

    @staticmethod
    def update_customer(customer_id: str, customer_data: CustomerUpdate) -> Customer:
        CustomerService._validate_customer_data(customer_data)
        CustomerService._authorize_request()
        customer = CustomerService._update_customer_in_db(customer_id, customer_data)
        CustomerService._log_update(customer_id)
        return customer

    @staticmethod
    def _validate_customer_data(customer_data):
        # Add validation logic here
        pass

    @staticmethod
    def _authorize_request():
        verify_token()

    @staticmethod
    def _create_customer_in_db(customer_data: CustomerCreate) -> Customer:
        try:
            result = customers_collection.insert_one(customer_data.dict())
            customer = customers_collection.find_one({"_id": result.inserted_id})
            return Customer(**customer)
        except Exception as e:
            logger.error(f"Error creating customer: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")

    @staticmethod
    def _log_creation(customer: Customer):
        log_action("create_customer", f"Customer created with ID: {customer.id}")

    @staticmethod
    def _update_customer_in_db(customer_id: str, customer_data: CustomerUpdate) -> Customer:
        try:
            result = customers_collection.update_one(
                {"_id": customer_id}, {"$set": customer_data.dict(exclude_unset=True)}
            )
            if result.matched_count == 0:
                log_action("update_customer", f"Customer with ID {customer_id} not found for update")
                raise HTTPException(status_code=404, detail="Customer not found")
            customer = customers_collection.find_one({"_id": customer_id})
            return Customer(**customer)
        except Exception as e:
            logger.error(f"Error updating customer: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")

    @staticmethod
    def _log_update(customer_id: str):
        log_action("update_customer", f"Customer with ID {customer_id} updated")