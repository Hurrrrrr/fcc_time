MINUTES_TO_HOURS = 60
MINUTES_IN_DAY = 1440
today = 0

def add_time(start_time, duration, day=None):

    parsed_input = parse_input(start_time, duration, day)

    start_in_minutes = time_to_minutes(parsed_input[0])
    duration_in_minutes = duration_to_minutes(parsed_input[1])

    end_time = minutes_to_time(start_in_minutes, duration_in_minutes)


    return



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



def set_day(parsed_day):

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



def minutes_to_time(start_in_minutes, duration_in_minutes):

    minutes = start_in_minutes + duration_in_minutes
    hours = 0
    days = 0
    time_AM = None
    time_days = 0
    time_hours = 0
    time_minutes = 0
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
    #######

    # result is multiple days later
    if start_in_minutes + duration_in_minutes >= (MINUTES_IN_DAY * 2):
        return

    #result is the next day
    if start_in_minutes + duration_in_minutes >= MINUTES_IN_DAY:
        return

    # result is same day
    if start_in_minutes + duration_in_minutes < MINUTES_IN_DAY:
        return


    

    
    # better to refactor to add days now
    



test_input = ("9:50 PM", "0:10", "tuesday")

parsed_test = parse_input(test_input[0], test_input[1])

print("Parsed input:", parsed_test)
print("Minutes:", time_to_minutes(parsed_test[0]))
print("Duration:", duration_to_minutes(parsed_test[1]))
