# utils/calculations.py

def calculate_health_quote(age, coverage_amount, pre_existing, smoker, quote_frequency):
    base_rate = 0.05  # Base rate per $1000 coverage
    age_factor = 0.01  # Additional charge per year of age
    if pre_existing:
        base_rate += 0.02  # Additional charge for pre-existing conditions
    if smoker:
        base_rate += 0.03  # Additional charge for smokers

    # Calculate total rate based on age
    total_rate = base_rate + (age_factor * (age - 18))  # Start charging from age 18
    # Calculate final quote amount (yearly)
    quote = coverage_amount * total_rate

    if quote_frequency == "Monthly":
        return quote / 12  # Convert to monthly
    else:
        return quote  # Return yearly quote


def calculate_auto_quote(vehicle_age, vehicle_value, coverage_type, vehicle_type, quote_frequency):
    base_rate = 0.03  # Base rate per $1000 vehicle value
    vehicle_type_factor = 0.0  # Factor for different vehicle types

    # Adjust base rate based on vehicle type
    if vehicle_type == "SUV":
        vehicle_type_factor = 0.01  # Lower risk for SUVs
    elif vehicle_type == "Truck":
        vehicle_type_factor = 0.02  # Higher risk for trucks
    elif vehicle_type == "Van":
        vehicle_type_factor = 0.005  # Lower risk for vans
    elif vehicle_type == "Sports Car":
        vehicle_type_factor = 0.03  # Higher risk for sports cars
    # Sedans are the base case with no additional factor

    if coverage_type == "Comprehensive":
        base_rate += 0.01  # Additional charge for comprehensive coverage
    elif coverage_type == "Collision":
        base_rate += 0.015  # Additional charge for collision coverage

    # Calculate total rate based on factors
    total_rate = base_rate + vehicle_type_factor
    quote = vehicle_value * total_rate

    if quote_frequency == "Monthly":
        return quote / 12  # Convert to monthly
    else:
        return quote  # Return yearly quote



def calcRentEstimate(rental_type, est_prop_val, desired_coverage):
    rate = 0.0
    if rental_type == "Apartment":
        rate = 0.03
    elif rental_type == "Condo":
        rate = 0.025
    elif rental_type == "Townhouse":
        rate = 0.06
    elif rental_type == "House":
        rate = 0.09
    return rate * desired_coverage * (est_prop_val / 0.6)
