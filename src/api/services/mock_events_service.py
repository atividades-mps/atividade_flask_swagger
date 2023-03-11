from src.domain.entities.event import Event
from src.domain.ports.events_service import EventsService


class MockEventsService(EventsService):
    def fetch_all(self) -> list[Event]:
        return []