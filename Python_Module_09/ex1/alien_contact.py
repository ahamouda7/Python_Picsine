from pydantic import model_validator
from typing import Optional
from pydantic import BaseModel, Field, ValidationError
from enum import Enum
from datetime import datetime


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0, le=10)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validator(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
                )
        if self.signal_strength > 7.0 and (not self.message_received):
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
                )
        return self


def main() -> None:
    print("\n     Alien Contact Log Validation")
    try:
        alien = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.fromisoformat("2026-04-18 18:46"),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5/10,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
        )

        print("=" * 40)
        print("Valid contact report:")
        print("=" * 40)

        print(f"ID: {alien.contact_id}")
        print(f"Type: {alien.contact_type.value}")
        print(f"Location: {alien.location}")
        print(f"Signal: {alien.signal_strength}")
        print(f"Duration: {alien.duration_minutes} minutes")
        print(f"Witnesses: {alien.witness_count}")
        print(f"Message: '{alien.message_received}'")

        print()
        print("=" * 40)
        print("Expected validation error:")
        print("=" * 40)

        AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.fromisoformat("2026-04-18 18:46"),
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5/10,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli",
        )
    except ValidationError as e:
        for error in e.errors():
            if error["msg"].startswith("Value error, "):
                error["msg"] = error["msg"].replace("Value error, ", "")
            print(error["msg"])
        print()


if __name__ == "__main__":
    main()
