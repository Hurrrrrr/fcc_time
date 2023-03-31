MINUTES_TO_HOURS = 60

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
        day_lower = day.lower()

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

    # format: [H, M, "AM/PM"], [H, M]
    return [start_time_parsed, duration_parsed]



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

    while minutes > 59:
        hours = hours + 1
        minutes = minutes - 60
    
    # better to refactor to add days now
    



test_input = ("9:50 PM", "3:10")

parsed_test = parse_input(test_input[0], test_input[1])

print("Parsed input:", parsed_test)
print("Minutes:", time_to_minutes(parsed_test[0]))
print("Duration:", duration_to_minutes(parsed_test[1]))
