import logging
import subprocess

class AuditLogMonitor:
    def __init__(self, log_file_path: str):
        self.log_file_path = log_file_path
        self.logger = logging.getLogger('AuditLogMonitor')
        self.logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler('logs/audit_log_monitor.log')
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(handler)

    def start_monitoring(self):
        self.logger.info("Starting log monitoring.")
        try:
            with open(self.log_file_path, 'r') as log_file:
                for line in log_file:
                    self.logger.debug(f"Log entry: {line.strip()}")
                    self.detect_suspicious_activity(line)
        except FileNotFoundError:
            self.logger.error(f"Log file {self.log_file_path} not found.")
        except Exception as e:
            self.logger.error(f"An error occurred while monitoring logs: {str(e)}")

    def detect_suspicious_activity(self, log_entry: str):
        self.logger.debug("Detecting suspicious activity.")
        if "suspicious" in log_entry.lower():
            self.logger.warning(f"Suspicious activity detected: {log_entry.strip()}")
            self.perform_security_check()

    def perform_security_check(self):
        self.logger.info("Performing security check using Nmap.")
        try:
            result = subprocess.run(['nmap', '-sP', 'localhost'], capture_output=True, text=True)
            self.logger.info(f"Nmap Output: {result.stdout}")
        except Exception as e:
            self.logger.error(f"An error occurred during the security check: {str(e)}")