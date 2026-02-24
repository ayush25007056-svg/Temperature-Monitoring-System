import random
import time

# Accept temperature limits
min_limit = float(input("Enter minimum temperature limit: "))
max_limit = float(input("Enter maximum temperature limit: "))

print("\nStarting IoT Temperature Monitoring System...\n")

while True:
    # Generate random temperature between -10 and 60
    temperature = round(random.uniform(-10, 60), 2)
    
    print("Current Temperature:", temperature, "°C")
    
    # Compare temperature with limits
    if temperature < min_limit:
        print("⚠ ALERT: Temperature is BELOW minimum limit!\n")
    elif temperature > max_limit:
        print("⚠ ALERT: Temperature is ABOVE maximum limit!\n")
    else:
        print("✅ Temperature is within safe limits.\n")
    
    # Wait for 2 seconds
    time.sleep(2)