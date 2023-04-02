MINUTES_TO_HOURS = 60
MINUTES_IN_DAY = 1440
today = 0

def add_time(start_time, duration, day=None):

    parsed_input = parse_input(start_time, duration, day)

    start_in_minutes = time_to_minutes(parsed_input[0])
    duration_in_minutes = duration_to_minutes(parsed_input[1])

    end_time = minutes_to_time(start_in_minutes, duration_in_minutes)


    return end_time



def parse_input(start_time, duration, day=None):

    start_time_parsed = []
    duration_parsed = []
    if day != None:
        day_parsed = day.lower()
        set_day(day_parsed)

    start_time_replaced = start_time.replace(" ", ":")

    start_split = start_time_replaced.split(":")
    duration_split = duration.split(":")

    for item in start_split:
        if item.isdigit():
            start_time_parsed.append(int(item))
        else:
            start_time_parsed.append(item)
    
    for item in duration_split:
        if item.isdigit():
            duration_parsed.append(int(item))
        else:
            duration_parsed.append(item)
    


    # format: [H, M, "AM/PM"], [H, M], ["day"]
    return [start_time_parsed, duration_parsed]



def set_day(day_parsed):

    if day_parsed == "monday":
        today = 1
    elif day_parsed == "tuesday":
        today = 2
    elif day_parsed == "wednesday":
        today = 3
    elif day_parsed == "thursday":
        today = 4
    elif day_parsed == "friday":
        today = 5
    elif day_parsed == "saturday":
        today = 6
    elif day_parsed == "sunday":
        today = 7


def time_to_minutes(parsed_start_time):

    my_time = parsed_start_time

    # change 12:XX to 00:XX to compensate for mandatory 12-hour clock input
    if my_time[0] == 12:
            my_time[0] = my_time[0] - 12
    
    if my_time[2] == "PM":
        my_time[0] = my_time[0] + 12
    
    minutes = ((my_time[0] * MINUTES_TO_HOURS) + my_time[1])
    
    return minutes



def duration_to_minutes(parsed_duration):

    minutes = (parsed_duration[0] * MINUTES_TO_HOURS) + parsed_duration[1]
    return minutes


# day is not a parameter because it's kept track of via global variable
def minutes_to_time(start_in_minutes, duration_in_minutes):

    minutes = start_in_minutes + duration_in_minutes
    hours = 0
    days = 0
    time_AM = None
    final_days = 0
    day_display_flag = -1
    clock_time = []

    while minutes >= MINUTES_IN_DAY:
        days = days + 1
        minutes = minutes - MINUTES_IN_DAY

    while minutes >= 60:
        hours = hours + 1
        minutes = minutes - 60
    
    if (hours % 24) <= 12:
        time_AM = True
    else:
        time_AM = False
        hours = hours - 12
    
    final_days = today + days

    # result is multiple days later
    if final_days - today >= 2:
        day_display_flag = 2

    # result is the next day
    if final_days - today == 1:
        day_display_flag = 1
    
    # user wants days displayed
    if today > 0:
        day_display_flag = 0
    
    clock_time.append(str(hours))
    clock_time.append(":")
    clock_time.append(str(minutes).zfill(2))
    clock_time.append(" ")
    if time_AM == True:
        clock_time.append("AM")
    else:
        clock_time.append("PM")
    
    output = "".join(clock_time)
    
    
    return output


    

    
    



test_input = ("3:30 PM", "10:30", "tuesday")

parsed_test = parse_input(test_input[0], test_input[1])

print("Parsed input:", parsed_test)
print("Minutes:", time_to_minutes(parsed_test[0]))
print("Duration:", duration_to_minutes(parsed_test[1]))
print("Output:", add_time(test_input[0], test_input[1], test_input[2]))
