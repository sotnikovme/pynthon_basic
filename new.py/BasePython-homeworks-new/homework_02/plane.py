from base import Vehicle
import exceptions

class Plane(Vehicle):
    def __init__(self, cargo, max_cargo):
        self.cargo = cargo
        self.max_cargo = max_cargo

def load_cargo(cargo):
    if cargo <= Plane.max_cargo:
        return cargo
    else:
        exceptions.CargoOverload
        print("Перегруз")

def remove_all_cargo():
    yield Plane.cargo
Plane.cargo = 0