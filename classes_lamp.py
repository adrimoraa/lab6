#base
class Lamp:
    def __init__(self, power, energy, lifetime):
        self.power = power          # radiation 
        self.energy = energy        # energy c
        self.lifetime = lifetime    # lifetime 

    def days_until_burnout(self):
        return self.lifetime / 8


#  Daylight lampppp
class DaylightLamp(Lamp):
    def __init__(self, power, energy, lifetime, color_temp):
        Lamp.__init__(self, power, energy, lifetime)
        self.color_temp = color_temp

    def power_energy_ratio(self):
        return self.power / self.energy


# Spotlightttt
class Spotlight(Lamp):
    def __init__(self, power, energy, lifetime, angle):
        Lamp.__init__(self, power, energy, lifetime)
        self.angle = angle

    def power_energy_ratio(self):
        return self.power / self.energy


# Mainnn
lamp1 = DaylightLamp(60, 10, 8000, 5000)
lamp2 = Spotlight(100, 20, 6000, 45)

print("Daylight lamp")
print("Days before burnout:", lamp1.days_until_burnout())
print("Power to energy:", lamp1.power_energy_ratio())

print()

print("Spotlight")
print("Days before burnout:", lamp2.days_until_burnout())
print("Power to energy :", lamp2.power_energy_ratio())
