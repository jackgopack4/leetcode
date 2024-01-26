class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # each hour is 30 degrees plus minutes*0.5
        if hour == 12:
            hour_angle = 0.0
        else:
            hour_angle = hour * 30.0
        hour_angle += minutes*0.5
        minute_angle = minutes*6.0
        
        test_angle = abs(minute_angle - hour_angle)

        if 360.0 - test_angle < test_angle:
            return 360.0 - test_angle
        else:
            return test_angle
