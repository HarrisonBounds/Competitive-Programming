#Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

def timeConversion(s):
    #s[8] will tell us am or pm
    str_h = s[0]
    str_h += s[1]
    
    initial = int(str_h)
    
    if s[8] == 'P':
        hour = (initial % 12) + 12
        string_hour = str(hour)
        
        
    else:
        if initial == 12:
            string_hour = "00"
        else:
            if initial < 10:
                string_hour = "0"
                string_hour += str(initial)
            else:
                string_hour = str(initial)
            
    string_hour += s[2:8]
    
    return string_hour
    