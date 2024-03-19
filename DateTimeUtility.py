from datetime import datetime

class DateTimeUtility:
    
    @staticmethod
    def get_cur_datetime():
        return datetime.now()
    
    @staticmethod
    def find_cur_difference(date_from):
        cur_date = datetime.now()
        if date_from < cur_date:
            time_diff = cur_date - date_from
            return time_diff
        else:
            time_diff = date_from - cur_date
            return time_diff
        
    
first_data = datetime(2024, 1, 10)
second_date = datetime(2025, 4, 11)
date_diff_past = DateTimeUtility.find_cur_difference(first_data)
date_diff_past2 = DateTimeUtility.find_cur_difference(second_date)

days = date_diff_past.days
remaining_seconds = date_diff_past.seconds
hours = remaining_seconds // 3600
remaining_seconds %= 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60


print("Days:", days)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)



