import datetime
from typing import Dict

class Alert:
    def __init__(self, event_type: str, actor: str, timestamp: datetime.datetime = None):
        self.event_type = event_type
        self.actor = actor
        self.timestamp = timestamp or datetime.datetime.now()

    def serialize(self) -> Dict[str, str]:
        return {
            'event_type': self.event_type,
            'actor': self.actor,
            'timestamp': self.timestamp.isoformat()
        }

    @staticmethod
    def deserialize(data: Dict[str, str]) -> 'Alert':
        return Alert(
            event_type=data['event_type'],
            actor=data['actor'],
            timestamp=datetime.datetime.fromisoformat(data['timestamp'])
        )