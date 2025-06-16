import logging
from fastapi import FastAPI
import uvicorn
from services.audit_log_monitor import AuditLogMonitor
from controllers.alert_controller import router as alert_router

# Initialize FastAPI app
app = FastAPI()

# Include routers
app.include_router(alert_router)

# Initialize and start the AuditLogMonitor
log_monitor = AuditLogMonitor(log_file_path='path/to/your/logfile.log')

@app.on_event("startup")
async def startup_event():
    logging.info("Starting AuditLogMonitor...")
    log_monitor.start_monitoring()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)