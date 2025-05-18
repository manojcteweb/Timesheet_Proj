import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("audit")

def log_action(action: str, detail: str):
    logger.info(f"Action: {action}, Detail: {detail}")