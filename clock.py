def convert24hour(hour, minute, period):
    #step 1: function named convert_to_24_hour that takes three parameters: hour, minute, and period.
    # Step 2: Check if the hour is 12. If it is, set hour to 0 to handle the cases of "12:00 am" and "12:00 pm."
    if hour == 12:
        hour = 0
    
    # Step 3: If the given period is "pm," add 12 to the hour. This converts the time to 24-hour format.
    if period.lower() == 'pm':
        hour += 12
    
    # Step 4: ensure that both hour and minute are represented 
    time_24_hour = "{:02d}{:02d}".format(hour, minute)

    # Step 5: Concatenate the formatted hour and minute as a four-digit string.

    return time_24_hour

# Step 6: Example Usage
time_24_hour_1 = convert24hour(8, 30, 'am')
print(time_24_hour_1)  # Output: 0830

time_24_hour_2 = convert24hour(8, 30, 'pm')
print(time_24_hour_2)  # Output: 2030
