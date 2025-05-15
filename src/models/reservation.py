from datetime import date
from typing import Dict, Any
import uuid

from .guest import Guest
from .room import Room

class Reservation:
    """Represents a reservation made by a guest for a specific room and time.

    Attributes:
        reservation_id (str): Unique ID for the reservation.
        guest (Guest): The guest making the reservation.
        room (Room): The room being reserved.
        check_in (date): The check-in date.
        check_out (date): The check-out date.
    """

    def __init__(self, guest: Guest, room: Room, check_in: date, check_out: date):
        """Initializes a Reservation object."""
        if not isinstance(guest, Guest):
            raise TypeError("guest must be an instance of Guest.")
        if not isinstance(room, Room):
            raise TypeError("room must be an instance of Room.")
        if not isinstance(check_in, date) or not isinstance(check_out, date):
            raise TypeError("check_in and check_out must be date objects.")
        if check_in >= check_out:
            raise ValueError("Check-out date must be after check-in date.")

        self.reservation_id: str = str(uuid.uuid4())
        self.guest: Guest = guest
        self.room: Room = room
        self.check_in: date = check_in
        self.check_out: date = check_out

    def get_duration(self) -> int:
        """Returns the number of nights of the stay."""
        return (self.check_out - self.check_in).days

    def get_total_price(self) -> float:
        """Calculates total cost for the stay."""
        return self.get_duration() * self.room.price_per_night

    def get_summary(self) -> Dict[str, Any]:
        """Returns a dictionary summary of the reservation."""
        return {
            "reservation_id": self.reservation_id,
            "guest_name": self.guest.get_full_name(),
            "room_number": self.room.number,
            "check_in": self.check_in.isoformat(),
            "check_out": self.check_out.isoformat(),
            "nights": self.get_duration(),
            "total_price": self.get_total_price(),
        }

    def __str__(self) -> str:
        return (f"Reservation {self.reservation_id}: {self.guest.get_full_name()} - "
                f"Room {self.room.number} from {self.check_in} to {self.check_out}")

    def __repr__(self) -> str:
        return (f"Reservation(reservation_id='{self.reservation_id}', "
                f"guest={repr(self.guest)}, room={repr(self.room)}, "
                f"check_in={self.check_in}, check_out={self.check_out})")