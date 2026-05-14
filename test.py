from cars import Car
from project import calculate_time

#tests to see if my calculate time actually works. Because a slower time is greater, a fast time should be lower than slower time.
fast= Car("fast",10,5,5,5)
slow = Car("slow",2,5,5,5)
fast_time = calculate_time(fast,500,0,0)
slow_time = calculate_time(slow,500,0,0)

if slow_time<fast_time:
    print("Code failed")
if fast_time<slow_time:
    print("Success")