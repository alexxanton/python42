from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")

    try:
        space_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(3078, 8, 1),
            is_operational=True,
        )

        status = (
            "Operational" if space_station.is_operational else "Broken"
        )
        print(
            "Valid station created:",
            f"ID: {space_station.station_id}",
            f"Name: {space_station.name}",
            f"Crew: {space_station.crew_size} people",
            f"Power: {space_station.power_level:.1f}%",
            f"Oxygen: {space_station.oxygen_level:.1f}%",
            f"Status: {status}",
            sep="\n"
        )
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"])

    print("\n========================================")
    print("Expected validation error:")

    try:
        invalid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=60,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(3078, 8, 1),
            is_operational=True,
        )
        print(invalid_station)
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"])


if __name__ == "__main__":
    main()
