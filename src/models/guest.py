import uuid
from typing import Dict, Any

class Guest:
    """Represents a hotel guest.

    Attributes:
        guest_id (str): A unique identifier for the guest.
        first_name (str): The guest's first name.
        last_name (str): The guest's last name.
        email (str): The guest's email address.
        phone_number (str): The guest's phone number.
    """
    def __init__(self, first_name: str, last_name: str, email: str, phone_number: str):
        """Initializes a Guest object with a unique ID."""
        if not first_name or not isinstance(first_name, str):
            raise ValueError("First name must be a non-empty string.")
        if not last_name or not isinstance(last_name, str):
             raise ValueError("Last name must be a non-empty string.")
        if not email or "@" not in email or "." not in email.split("@")[1]:
             raise ValueError("Invalid email format.")
        if not phone_number or not isinstance(phone_number, str):
             raise ValueError("Phone number must be a non-empty string.")


        self.guest_id: str = str(uuid.uuid4()) # id dla guesta (moze tez nr tel byc jako id bo jest unikalny?)
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.email: str = email
        self.phone_number: str = phone_number

    def get_full_name(self) -> str:
        """Returns the guest's full name.

        Returns:
            str: The concatenated first and last name.
        """
        return f"{self.first_name} {self.last_name}"

    def get_contact_info(self) -> Dict[str, str]:
        """Returns the guest's contact information.

        Returns:
            Dict[str, str]: A dictionary with email and phone number.
        """
        return {"email": self.email, "phone_number": self.phone_number}

    def __str__(self) -> str:
        """Returns a string representation of the guest."""
        return f"Guest: {self.get_full_name()} (ID: {self.guest_id})"

    def __repr__(self) -> str:
        """Returns an official string representation of the guest."""
        return (f"Guest(guest_id='{self.guest_id}', first_name='{self.first_name}', "
                f"last_name='{self.last_name}', email='{self.email}', "
                f"phone_number='{self.phone_number}')")