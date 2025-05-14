from typing import List, Optional, Dict, Any

from .room import Room

class Hotel:
    """Represents the hotel, managing a collection of rooms.

    Attributes:
        name (str): The name of the hotel.
        address (str): The physical address of the hotel.
        rooms (Dict[str, Room]): A dictionary mapping room numbers to Room objects.
    """
    def __init__(self, name: str, address: str):
        """Initializes a Hotel object."""
        if not name or not isinstance(name, str):
             raise ValueError("Hotel name must be a non-empty string.")
        if not address or not isinstance(address, str):
             raise ValueError("Hotel address must be a non-empty string.")

        self.name: str = name
        self.address: str = address
        self.rooms: Dict[str, Room] = {}

    def add_room(self, room: Room) -> None:
        """Adds a room to the hotel.

        Args:
            room (Room): The Room object to add.

        Raises:
            ValueError: If a room with the same number already exists.
        """
        if not isinstance(room, Room):
            raise TypeError("Can only add Room objects.")
        if room.number in self.rooms:
            raise ValueError(f"Room with number {room.number} already exists in this hotel.")
        self.rooms[room.number] = room
        print(f"Room {room.number} added to {self.name}.")

    def find_room_by_number(self, number: str) -> Optional[Room]:
        """Finds a room by its number.

        Args:
            number (str): The room number to search for.

        Returns:
            Optional[Room]: The Room object if found. None otherwise.
        """
        return self.rooms.get(number)

    def get_all_rooms(self) -> List[Room]:
         """Returns a list of all rooms in the hotel."""
         return list(self.rooms.values())

    # do zrobienia: sprawdzenie dostępności z datami musi odbyć się w ReservationSystem, który ma dostęp do klasy rezerwacji.
    def filter_rooms(self, room_type: Optional[str] = None, capacity: Optional[int] = None) -> List[Room]:
        """Filters rooms based on type and/or capacity.

        Args:
            room_type (Optional[str]): The desired room type.
            capacity (Optional[int]): The minimum desired capacity.

        Returns:
            List[Room]: A list of rooms matching the criteria.
        """
        filtered_list = list(self.rooms.values())

        if room_type:
            filtered_list = [r for r in filtered_list if r.room_type.lower() == room_type.lower()]

        if capacity:
            filtered_list = [r for r in filtered_list if r.capacity >= capacity]

        return filtered_list

    def __str__(self) -> str:
        return f"Hotel: {self.name} ({self.address}) - {len(self.rooms)} rooms."

    def __repr__(self) -> str:
        return f"Hotel(name='{self.name}', address='{self.address}')"