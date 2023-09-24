def add_time(start_time , duration , weekday=None):
    new_time = None
    days = {
        1 : 'monday', 
        2 : 'tuesday',
        3 : 'wednesday',
        4 : 'thursday',
        5 : 'friday',
        6 : 'saturday',
        7 : 'sunday'
    }


    m = start_time.split()[1]
    hr , mins = ((start_time.split()[0]).split(':'))
    hr , mins = int(hr) , int(mins)
    dur_hrs , dur_mins = (duration.split(':'))
    dur_hrs , dur_mins = int(dur_hrs) , int(dur_mins)

    if m == 'AM' and hr == 12:
        hr == 0
    if m == 'PM':
        hr += 12
    
    new_hrs , new_mins = hr + dur_hrs , mins + dur_mins
    if new_mins > 60:
        new_hrs += 1
        new_mins -= 60

    # if the time goes to the next day 
    day = 0
    message = None
    if new_hrs > 23:
        day , hours = divmod(new_hrs , 24)
        final_hours = hr + hours
        if day == 1:
            message = '(next day)'
        elif day > 1:
            message = f'({day} days later)'

    final_hours = new_hrs
    final_mins = new_mins
    
    # back to 12 hr

    qoutient ,remainder = divmod(final_hours, 12)
    final_hours = remainder

    if final_hours == 0:
        final_hours = 12

    if qoutient % 2 == 0:
        m = 'AM'
    elif qoutient % 2 != 0:
        m = 'PM'

    if final_hours == 12 and qoutient % 2 == 0:
        m = 'AM'
    elif final_hours == 12 and qoutient % 2 != 0:
        m = 'PM'

        
####################################    


    the_time = f'{final_hours}:{final_mins:02d} {m}'
    
     
    if weekday:
        weekday = weekday.lower()
        values = list(days.values()) # days

        n = values.index(weekday)
        if day > 0 and day < 8:
            n = values.index(weekday) + day

        if n > 7:
            x = divmod(n , 7)[1]
            weekday = days[n + x]
        elif n < 7:
            weekday = days[n]

        if n == 1:
            weekday = days[0]
        
        if message:
            new_time = f'{the_time}, {weekday.title()} {message}'
        else:
            new_time = f'{the_time}, {weekday.title()}'
    
    else:
        if message:
            new_time = f'{the_time} {message}'
        else:
            new_time = the_time

    return new_time    






    
    


