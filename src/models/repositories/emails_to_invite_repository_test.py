from .emails_to_invite_repository import EmailsToInviteRepository
from src.models.settings.db_connection_handler import db_connection_handler
import uuid
import pytest

db_connection_handler.connect()
trip_id = str(uuid.uuid4())


@pytest.mark.skip(reason="db integration")
def test_registry_email():
    connection = db_connection_handler.get_connection()
    emails_to_trip_repository = EmailsToInviteRepository(connection)
    
    email_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "email":"ruan@email.com"
    }
    
    emails_to_trip_repository.registry_email(email_infos)
    
@pytest.mark.skip(reason="db integration")
def test_find_emails_from_trip():
    connection = db_connection_handler.get_connection()
    emails_to_trip_repository = EmailsToInviteRepository(connection)
    
    trip = emails_to_trip_repository.find_emails_from_trip(trip_id)
    print()
    print(trip) 
