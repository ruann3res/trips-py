from .trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler
import uuid
from datetime import datetime, timedelta
import pytest

db_connection_handler.connect()
trip_id = str(uuid.uuid4())


@pytest.mark.skip(reason="db integration")
def test_create_trip():
    connection = db_connection_handler.get_connection()
    trips_repository = TripsRepository(connection)
    
    trips_infos = {
        "id": trip_id,
        "destination":"Uberlândia",
        "start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
        "end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
        "owner_name": "Ruan Neres",
        "owner_email":"ruan@email.com"
    }
    
    trips_repository.create_trip(trips_infos)
    
@pytest.mark.skip(reason="db integration")
def test_find_trip_by_id():
    connection = db_connection_handler.get_connection()
    trips_repository = TripsRepository(connection)
    
    trip = trips_repository.find_trip_by_id(trip_id)
    print()
    print(trip) 

@pytest.mark.skip(reason="db integration")
def test_update_trip_status():
    connection = db_connection_handler.get_connection()
    trips_repository = TripsRepository(connection)
    
    trip = trips_repository.update_trip_status(trip_id)
    
    
    
    
     