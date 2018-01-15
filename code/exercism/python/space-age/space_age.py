class SpaceAge(object):
    earth_year = 31557600
    orbital_ratios = {
        'Earth': 1,
        'Mercury': 0.2408467,
        'Venus': 0.61519726,
        'Mars': 1.8808158,
        'Jupiter': 11.862615,
        'Saturn': 29.447498,
        'Uranus': 84.016846,
        'Neptune': 164.79132
    }

    def __init__(self, seconds):
        self.seconds = seconds
        self.year = self.seconds / self.earth_year

    def on_mercury(self):
        return round(self.year / self.orbital_ratios['Mercury'], 2)

    def on_venus(self):
        return round(self.year / self.orbital_ratios['Venus'], 2)

    def on_earth(self):
        return round(self.year / self.orbital_ratios['Earth'], 2)

    def on_mars(self):
        return round(self.year / self.orbital_ratios['Mars'], 2)

    def on_jupiter(self):
        return round(self.year / self.orbital_ratios['Jupiter'], 2)

    def on_saturn(self):
        return round(self.year / self.orbital_ratios['Saturn'], 2)

    def on_uranus(self):
        return round(self.year / self.orbital_ratios['Uranus'], 2)

    def on_neptune(self):
        return round(self.year / self.orbital_ratios['Neptune'], 2)
