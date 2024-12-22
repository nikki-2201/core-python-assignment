def calculate_fare(distance):
    base_fare = 50
    distance_fare = 10
    return base_fare + (distance * distance_fare)

def main():
    try:
        trips_input = input("Enter distances for trips separated by commas: ").strip()
        
        if not trips_input:
            print("No trips provided!")
            return
        
        trips = list(map(int, trips_input.split(',')))

        if any(trip <= 0 for trip in trips):
            print("Distance must be a positive number!")
            return

        total_fare = 0

        for i, trip in enumerate(trips, 1):
            fare = calculate_fare(trip)
            print(f"Trip {i}: ${fare:.2f}")
            total_fare += fare

        print(f"Total Fare: ${total_fare:.2f}")

    except ValueError:
        print("Invalid input! Please enter valid numeric distances.")

if __name__ == "__main__":
    main()
