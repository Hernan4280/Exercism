class SpaceAge:
    EARTH_SECONDS = 31557600

    ORBITAL_PERIODS = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1.0,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }

    def __init__(self, seconds: int):
        self.seconds = seconds

    def _on_planet(self, planet: str) -> float:
        years = self.seconds / (self.EARTH_SECONDS * self.ORBITAL_PERIODS[planet])
        return round(years, 2)

    def on_mercury(self) -> float:
        return self._on_planet("mercury")

    def on_venus(self) -> float:
        return self._on_planet("venus")

    def on_earth(self) -> float:
        return self._on_planet("earth")

    def on_mars(self) -> float:
        return self._on_planet("mars")

    def on_jupiter(self) -> float:
        return self._on_planet("jupiter")

    def on_saturn(self) -> float:
        return self._on_planet("saturn")

    def on_uranus(self) -> float:
        return self._on_planet("uranus")

    def on_neptune(self) -> float:
        return self._on_planet("neptune")
