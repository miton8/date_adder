import sys

class mydate():
    def __init__(self, input_date):
        try:
            self.day, self.month, self.year = input_date.split('.')
            self.day = int(self.day)
            self.month = int(self.month)
            self.year = int(self.year)
        except:
            raise KeyError("Wrong input data")
        if self.month>12:
            raise KeyError('Month cannot be grater than 12')
        self.days_in_month = self.get_days_in_month()
        if self.day>self.days_in_month:
            raise KeyError('Given month only has {} days'.format(self.days_in_month))
    def __str__(self):
        return "{}.{}.{}".format(self.day, self.month, self.year)
    def add(self, num_of_days):
        for day in range(num_of_days):
            self.day +=1
            if self.day > self.days_in_month:
                self.day = 1
                self.month +=1
                if self.month > 12:
                    self.month = 1
                    self.year += 1
                self.days_in_month = self.get_days_in_month()
    def get_days_in_month(self):
        days_in_month_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        if self.year % 400 == 0 or (self.year % 4 == 0 and self.year % 100 != 0):
            days_in_month_dict[2]=29
        return days_in_month_dict[self.month]

def add_days(input_date, number_of_days):
    date = mydate(input_date)
    date.add(number_of_days)
    print(date)
    


if __name__ == "__main__":

    input_date = '29.06.2020'
    number_of_days = 8

    if len (sys.argv) > 1:
        input_date = sys.argv[1] 
        number_of_days = int(sys.argv[2])
    
    add_days(input_date, number_of_days)
    

    



        