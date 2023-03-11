from flask import Blueprint

from src.api.services.mock_events_service import MockEventsService
from src.domain.use_cases.fetch_all_events import FetchAllEvents

events_blueprint = Blueprint('events', __name__)

@events_blueprint.get('/events')
def fetch_all():
    fetch_all_events = FetchAllEvents(MockEventsService())
    return fetch_all_events.execute()