from sqlite3 import Connection
from typing import Dict, Tuple, List

class LinksToTripRepository:
    def __init__(self, connection: Connection) -> None:
        self.__connection = connection

    def registry_link(self, link_infos: Dict) -> None:
        cursor = self.__connection.cursor()
        cursor.execute(
            '''
                INSERT INTO links
                    (id, trip_id, link, title)
                VALUES
                    (?, ?, ?, ?)
            ''', (
                link_infos["id"],
                link_infos["trip_id"],
                link_infos["link"],
                link_infos["title"],
            )
        )
        self.__connection.commit()
    def find_links_from_trip(self, trip_id:str) -> List[Tuple]:
        cursor = self.__connection.cursor()
        cursor.execute( '''SELECT * FROM links WHERE trip_id = ?''', (trip_id,) )
        
        links = cursor.fetchall()
        return links
    