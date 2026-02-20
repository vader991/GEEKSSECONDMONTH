class Distance:

    _conversion_to_meters = {
        "cm": 0.01,
        "m": 1,
        "km": 1000
    }

    def __init__(self, value, unit):
        if unit not in self._conversion_to_meters:
            raise ValueError("Недопустимая единица измерения")
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def _to_meters(self):
        return self.value * self._conversion_to_meters[self.unit]

    def _from_meters(self, meters, target_unit):
        return meters / self._conversion_to_meters[target_unit]

    def __add__(self, other):
        if not isinstance(other, Distance):
            raise TypeError("Можно складывать только Distance с Distance")

        total_meters = self._to_meters() + other._to_meters()

        
        new_value = self._from_meters(total_meters, self.unit)
        return Distance(new_value, self.unit)

    def __sub__(self, other):
        if not isinstance(other, Distance):
            raise TypeError("Можно вычитать только Distance  из Distance")

        total_meters = self._to_meters() - other._to_meters()
        new_value = self._from_meters(total_meters, self.unit)
        return Distance(new_value, self.unit)



d1 = Distance(10, "m")
d2 = Distance(2, "km")
d3 = Distance(300, "cm")

print(d1)
print(d2)
print(d3)

print(d1 + d2)
print(d2 + d1)
print(d1 + d3)

print(d2 - d1)
