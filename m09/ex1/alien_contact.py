from pydantic import BaseModel, Field, ValidationError, model_validator
from typing_extensions import Self
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValidationError("contact_id must start with 'AC'")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValidationError("Physical contact must be verified")
        if self.contact_type == ContactType.TELEPATHIC:
            if witness_count < 3:
                raise ValidationError(
                    "Telepathic contact requires at least 3 witnesses"
                )
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValidationError(
                "Strong signals should include received messages"
            )

        return self

def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")

    try:
        alien_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(3450, 1, 1),
            location="Area 51, Nevada",
            contact_type="radio",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
    except ValidationError as e:
        print(e)

    print(
        f"ID: {alien_contact.contact_id}",
        f"Type: {alien_contact.contact_type}",
        f"Location: {alien_contact.location}",
        f"Signal: {alien_contact.signal_strength}/10",
        f"Duration: {alien_contact.duration_minutes} minutes",
        f"Witnesses: {alien_contact.witness_count}",
        f"Message: '{alien_contact.message_received}'",
        sep="\n"
    )


if __name__ == "__main__":
    main()
