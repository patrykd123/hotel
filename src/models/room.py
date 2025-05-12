from typing import Dict, Any

class Room:
    """Represents a hotel room.

    Attributes:
        number (str): The unique room number.
        room_type (str): The type of the room (e.g., 'single', 'double', 'suite').
        price_per_night (float): The cost for one night stay in this room.
        capacity (int): The maximum number of guests the room can accommodate.
    """
    def __init__(self, number: str, room_type: str, price_per_night: float, capacity: int):
        """Initializes a Room object."""
        if not isinstance(number, str) or not number:
            raise ValueError("Room number must be a non-empty string.")
        if not isinstance(room_type, str) or not room_type:
            raise ValueError("Room type must be a non-empty string.")
        if not isinstance(price_per_night, (int, float)) or price_per_night <= 0:
            raise ValueError("Price per night must be a positive number.")
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")

        self.number: str = number
        self.room_type: str = room_type
        self.price_per_night: float = float(price_per_night)
        self.capacity: int = capacity

    def get_details(self) -> Dict[str, Any]:
        """Returns the room's details as a dictionary.

        Returns:
            Dict[str, Any]: A dictionary containing room attributes.
        """
        return {
            "number": self.number,
            "room_type": self.room_type,
            "price_per_night": self.price_per_night,
            "capacity": self.capacity,
        }

    def __str__(self) -> str:
        """Returns a string representation of the room."""
        return (f"Room {self.number} ({self.room_type}, Capacity: {self.capacity}, "
                f"Price: ${self.price_per_night:.2f}/night)")

    def __repr__(self) -> str:
        """Returns an official string representation of the room."""
        return (f"Room(number='{self.number}', room_type='{self.room_type}', "
                f"price_per_night={self.price_per_night}, capacity={self.capacity})")