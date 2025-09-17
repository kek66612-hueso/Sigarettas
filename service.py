from repository import FlightRepository
from flight import Flight

class FlightService:
    def __init__(self,repository:FlightRepository):
        self.repository = repository

    def create_flight(self, flight:Flight):

        return self.repository.create_flight(flight)
    
    def get_all(self):

        return self.repository.get_all()
        
    def get_by_id(self,flight_id:int):

        return self.repository.get_by_id(flight_id)
    
    def update_flight(self, flight:Flight):

        return self.repository.update_flight(flight)
    
    def delete_flight(self,flight_id:int):

        return self.repository.delete_flight(flight_id)