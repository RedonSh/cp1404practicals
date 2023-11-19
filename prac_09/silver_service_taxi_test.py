from silver_service_taxi import SilverService

my_silver_taxi = SilverService("Prius 1", 200, 2)
distance = 18
my_silver_taxi.drive(distance)
fare = my_silver_taxi.get_fare()

print(
    f"For a {distance} km trip in a {my_silver_taxi.name} with fanciness of {my_silver_taxi.fanciness}, the fare is: ${fare:.2f}")
