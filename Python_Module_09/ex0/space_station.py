from typing import Optional
from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


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
    print("\n     Space Station Data Validation")
    try:
        station = SpaceStation(
            station_id="SS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.fromisoformat("2026-04-18T14:30:00")
            # I can pass: "2026-04-18 14:30:00" or "2026-04-18"
            )

        print("=" * 40)
        print("Valid station created:")
        print("=" * 40)

        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")

        if station.is_operational:
            print("Status: Operational\n")
        else:
            print("Status: Not operational\n")

        print("=" * 40)
        print("Expected validation error:")
        print("=" * 40)

        SpaceStation(
            station_id="SS001",
            name="International Space Station",
            crew_size=30,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.fromisoformat("2026-04-18")
            # I can use: "last_maintenance=datetime.fromtimestamp(1776522600)"
            )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])
        print()


if __name__ == "__main__":
    main()
