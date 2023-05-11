def temperature_fuzzy(temperature):
    if temperature <= 10:
        return "very_cold"
    elif temperature > 10 and temperature <= 20:
        return "slightly_cold"
    elif temperature > 20 and temperature <= 30:
        return "no_change"
    elif temperature > 30 and temperature <= 40:
        return "slightly_warm"
    else:
        return "very_warm"

# Set temperature input value and compute fuzzy value output
room_temperature = int(input('enter room temp: '))
fuzzy_value = temperature_fuzzy(room_temperature)

# Print fuzzy value output
print(fuzzy_value)
