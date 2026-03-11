from pydantic import BaseModel, Field, ValidationError, model_validator
from typing_extensions import Self
from datetime import datetime
from typing import List
from enum import Enum


class Rank(Enum):
    """List of crew ranks"""
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """Base model class for crew members validation"""
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """Base model class for space mission validation"""
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_requirements(self) -> Self:
        """Validates required values"""
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        if not any([
            member.rank in [Rank.CAPTAIN, Rank.COMMANDER]
            for member in self.crew
        ]):
            raise ValueError("Must have at least one Commander or Captain")
        if self.duration_days > 365:
            if any([member.years_experience < 5 for member in self.crew]):
                raise ValueError(
                    "Long missions (>365 days) need 5+ years experienced crew"
                )
        if not all([member.is_active for member in self.crew]):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    """Tests validation with valid and invalid values"""
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")

    try:
        space_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2026, 7, 1, 9, 0),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="sc01",
                    name="Sarah Connor",
                    rank=Rank.COMMANDER,
                    age=30,
                    specialization="Mission Command",
                    years_experience=5,
                ),
                CrewMember(
                    member_id="js01",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=30,
                    specialization="Navigation",
                    years_experience=5,
                ),
                CrewMember(
                    member_id="aj01",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=25,
                    specialization="Engineering",
                    years_experience=5,
                )
            ],
            mission_status="planned",
            budget_millions=2500.0
        )
        print(
            f"Mission: {space_mission.mission_name}",
            f"ID: {space_mission.mission_id}",
            f"Destination: {space_mission.destination}",
            f"Duration: {space_mission.duration_days} days",
            f"Budget: ${space_mission.budget_millions}M",
            f"Crew size: {len(space_mission.crew)}",
            sep="\n"
        )
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"])

    print("\n=========================================")
    print("Expected validation error:")

    try:
        invalid_mission = SpaceMission(
            mission_id="M3024_MARS",
            mission_name="Mars Colony War",
            destination="Mars",
            launch_date=datetime(3024, 7, 1, 9, 0),
            duration_days=100,
            crew=[
                CrewMember(
                    member_id="zrp01",
                    name="Zorp",
                    rank=Rank.CADET,
                    age=56,
                    specialization="Alien War Strats",
                    years_experience=42,
                )
            ],
            mission_status="planned",
            budget_millions=10000.0
        )
        print(invalid_mission)
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"])


if __name__ == "__main__":
    main()
