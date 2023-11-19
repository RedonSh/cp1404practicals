from unreliable_car import UnreliableCar

my_car = UnreliableCar("Prius 1", fuel=50, reliability=70)

for i in range(5):
    distance = 20  # Distance to drive
    distance_driven = my_car.drive(distance)

    if distance_driven > 0:
        print(f"Successfully drove {distance_driven} km.")
    else:
        print("Car failed to drive!")

print(f"\nCar Details: {my_car}")
