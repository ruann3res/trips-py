from .links_to_trip_repository import LinksToTripRepository
from src.models.settings.db_connection_handler import db_connection_handler
import uuid
import pytest

db_connection_handler.connect()
trip_id = str(uuid.uuid4())


def test_registry_link():
    connection = db_connection_handler.get_connection()
    links_to_trip_repository = LinksToTripRepository(connection)
    
    link_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "link":"http://any_url_link.com",
        "title":"any_tittle"
    }
    
    links_to_trip_repository.registry_link(link_infos)
    
# # @pytest.mark.skip(reason="db integration")
def test_find_links_from_trip():
    connection = db_connection_handler.get_connection()
    links_to_trip_repository = LinksToTripRepository(connection)
    
    response = links_to_trip_repository.find_links_from_trip(trip_id)

    assert isinstance(response, list)
    assert isinstance(response[0], tuple)
    
