# In order to prevent magic numbers:
# 1/60 = how many minutes in an hours
# 1/3600 = how many seconds in an hour
# 60 = how many minutes in an hour
# 1/60 = how many seconds in one minute
# 3600 = how many hours in seconds
# 60 = how many seconds in a minute

class TimeCalculator:
    # Starts the program by setting the elements equal to zero
    def __init__(self):
        self.__hours = 0
        self.__minutes = 0
        self.__seconds = 0

    # This function sets the number of hours given
    def setHours(self, hours):
        self.__hours = hours

    # This function sets the number of minutes given
    def setMinutes(self, minutes):
        self.__minutes = minutes

    # This function sets the number of seconds given
    def setSeconds(self, seconds):
        self.__seconds = seconds

    # This function converts minutes to hours and seconds to hours
    def time_in_Hours(self):
        min_in_hours = 1/60
        mins_in_hours = min_in_hours * self.__minutes
        second_in_hours = 1/3600
        seconds_in_hours = second_in_hours * self.__seconds
        return self.__hours + mins_in_hours + seconds_in_hours

    # This function converts hours to minutes and seconds to minutes
    def time_in_minutes(self):
        hour_in_mins = 60
        hours_in_mins = hour_in_mins * self.__hours
        second_in_mins = 1/60
        seconds_in_mins = second_in_mins * self.__seconds
        return self.__minutes + hours_in_mins + seconds_in_mins

    # # This function converts number of hours to seconds and minutes to seconds
    def time_in_seconds(self):
        hour_in_seconds = 3600
        hours_in_seconds = hour_in_seconds * self.__hours
        minute_in_seconds = 60
        minutes_in_seconds = minute_in_seconds * self.__minutes
        return self.__seconds + hours_in_seconds + minutes_in_seconds


def driver():
    test_time = TimeCalculator()
    test_time.setHours()
    test_time.setMinutes()
    test_time.setSeconds()

if __name__ == '__main__':
    driver()