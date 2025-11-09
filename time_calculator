def add_time(start_time, duration_time, day_of_the_week=''):

    left_st, right_st = start_time.split()
    hours_start_time, minutes_start_time = left_st.split(':')
    hours_duration_time, minutes_duration_time = duration_time.split(':')

    hours_start_time_int = int(hours_start_time)
    minutes_start_time_int = int(minutes_start_time)
    hours_duration_time_int = int(hours_duration_time)
    minutes_duration_time_int = int(minutes_duration_time)

    if right_st == 'PM' and hours_start_time_int != 12:
        hours_start_time_int += 12
    elif right_st == 'AM' and hours_start_time_int == 12:
        hours_start_time_int = 0 

    st_in_minutes = hours_start_time_int * 60 + minutes_start_time_int
    dt_in_minutes = hours_duration_time_int * 60 + minutes_duration_time_int
    result_in_minutes = st_in_minutes + dt_in_minutes

    days_later = result_in_minutes // 1440
    current_minutes = result_in_minutes % 1440

    days_text = ''
    if days_later == 1:
        days_text = '(next day)'
    elif days_later > 1:
        days_text = f'({days_later} days later)'

    weeks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    day_number = 0
    if day_of_the_week:
        if day_of_the_week.lower() == 'monday':
            day_number = 0
        elif day_of_the_week.lower() == 'tuesday':
            day_number = 1
        elif day_of_the_week.lower() == 'wednesday':
            day_number = 2
        elif day_of_the_week.lower() == 'thursday':
            day_number = 3
        elif day_of_the_week.lower() == 'friday':
            day_number = 4
        elif day_of_the_week.lower() == 'saturday':
            day_number = 5
        elif day_of_the_week.lower() == 'sunday':
            day_number = 6

        day_number = (day_number + days_later) % 7  

        day_suffix = f', {weeks[day_number]}' 
    else:
        day_suffix = '' 

    hour24 = current_minutes // 60
    minute  = current_minutes % 60

    period = ''
    if hour24 == 0:
        hour24 = 12
        period = "AM"
    elif 1 <= hour24 <= 11:
        period = "AM"
    elif hour24 == 12:
        period = "PM"
    elif hour24 > 12:
        hour24 = hour24 - 12
        period = "PM"

    minute_str = f'{minute:02d}'

    result = f'{hour24}:{minute_str} {period}{day_suffix} {days_text}'.strip()

    return result


print(add_time('3:30 PM', '2:12'))                      # 5:42 PM
print('5:42 PM')
print(add_time('11:43 PM', '24:20', 'tueSday'))         # 12:03 AM, Wednesday (next day)
print(add_time('2:59 AM', '24:00', 'saturDay'))         # 2:59 AM, Sunday (next day)
print(add_time('8:16 PM', '466:02', 'tuesday'))         # 6:18 AM, Monday (20 days later)
