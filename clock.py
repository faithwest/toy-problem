def convert24hour(hour, minute, period):
    # function named convert_to_24_hour that takes three parameters: hour, minute, and period.
    #  Check if the hour is 12. If it is, set hour to 0 to handle the cases of "12:00 am" and "If the hour is 12 and the period is "pm," leave the hour as is."
    if hour == 12:
        hour = 0
    
    # If the given period is "pm," add 12 to the hour. This converts the time to 24-hour format.
    if period.lower() == 'pm':
        hour += 12
    
    # ensure that both hour and minute are represented 
    time_24_hour = "{:02d}{:02d}".format(hour, minute)

    # Concatenate the formatted hour and minute as a four-digit string.

    return time_24_hour

