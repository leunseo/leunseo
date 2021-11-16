class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def is_valid_time(self,21,09,59):
        if {0}>24 or {1}>60 or {1}>60:
             print('{0}:{1}:{2}는 존재하지 않는 시간입니다.'.format(self.hour, self.minute, self.second))
        else:
             print('{0}:{1}:{2}는 존재하는 시간입니다.'.format(self.hour, self.minute, self.second))
                
    def is_valid_time(self,23,59,60):
        if {0}>24 or {1}>60 or {1}>60:
             print('{0}:{1}:{2}는 존재하지 않는 시간입니다.'.format(self.hour, self.minute, self.second))
        else:
             print('{0}:{1}:{2}는 존재하는 시간입니다.'.format(self.hour, self.minute, self.second))
