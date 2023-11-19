from taxi import Taxi

my_taxi = Taxi("Prius 1", 100)

my_taxi.drive(40)

print("Taxi Details after driving 40 km:")
print(my_taxi)
print(f"Current Fare: ${my_taxi.get_fare():.2f}")

my_taxi.start_fare()

my_taxi.drive(100)

print("\nTaxi Details after driving 100 km:")
print(my_taxi)
print(f"Current Fare: ${my_taxi.get_fare():.2f}")
