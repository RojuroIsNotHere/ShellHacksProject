# utils/calculations.py

def calculate_health_quote(age, pre_existing, coverage_amount):
    base_rate = 0.05  # Base rate per $1000 coverage
    age_factor = 0.01  # Additional charge per year of age
    if pre_existing:
        base_rate += 0.02  # Additional charge for pre-existing conditions

    # Calculate total rate based on age
    total_rate = base_rate + (age_factor * (age - 18))  # Start charging from age 18
    return coverage_amount * total_rate


def calculate_auto_quote(vehicle_age, vehicle_value, coverage_type):
    base_rate = 0.03  # Base rate per $1000 vehicle value
    if coverage_type == "Comprehensive":
        base_rate += 0.01  # Additional charge for comprehensive coverage
    elif coverage_type == "Collision":
        base_rate += 0.015  # Additional charge for collision coverage
    return vehicle_value * base_rate


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
