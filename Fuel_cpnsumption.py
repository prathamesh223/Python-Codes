def fuel_consumption():
    try:
        # Get user input for liters and distance, validate input
        liters = float(input("Enter the no of liters to fill the tank: "))
        kilometers = float(input("Enter the distance covered (in kilometers): "))

        # Validate input for non-positive values
        if liters <= 0 or kilometers <= 0:
            print("Invalid Input")
            return

        # Precompute conversion factors
        KM_TO_MILES = 0.6214
        LITERS_TO_GALLONS = 0.2642

        # Calculate fuel consumption in both formats
        liters_per_100km = (liters / kilometers) * 100
        miles = kilometers * KM_TO_MILES
        gallons = liters * LITERS_TO_GALLONS
        miles_per_gallon = miles / gallons

        # Display the results with two decimal precision
        print(f"Liters/100KM: {liters_per_100km:.2f}")
        print(f"Miles/gallons: {miles_per_gallon:.2f}")

    except ValueError:
        print("Invalid Input. Please enter numeric values.")

# Call the function
fuel_consumption()
