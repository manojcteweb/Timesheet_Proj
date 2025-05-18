from fastapi import APIRouter, Depends
from services.customer_service import CustomerService
from schemas.customer_schema import CustomerCreate, CustomerUpdate
from security.auth import verify_token

router = APIRouter()

@router.post("/customers", dependencies=[Depends(verify_token)])
def create_customer(customer_data: CustomerCreate):
    return CustomerService.create_customer(customer_data)

@router.get("/customers/{customer_id}", dependencies=[Depends(verify_token)])
def get_customer(customer_id: str):
    return CustomerService.get_customer(customer_id)

@router.put("/customers/{customer_id}", dependencies=[Depends(verify_token)])
def update_customer(customer_id: str, customer_data: CustomerUpdate):
    return CustomerService.update_customer(customer_id, customer_data)

@router.delete("/customers/{customer_id}", dependencies=[Depends(verify_token)])
def delete_customer(customer_id: str):
    CustomerService.delete_customer(customer_id)
    return {"detail": "Customer deleted"}
