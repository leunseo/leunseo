class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def is_valid_time(self,):
        if self.hour>24 or self.minute>60 or self.second>60:
             print('{0}:{1}:{2}는 존재하지 않는 시간입니다.'.format(self.hour, self.minute, self.second))
        else:
             print('{0}:{1}:{2}는 존재하는 시간입니다.'.format(self.hour, self.minute, self.second))
