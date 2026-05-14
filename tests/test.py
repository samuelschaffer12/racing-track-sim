import sys
import os

#had to get help for this line below
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cars import Car
from project import calculate_time,track_analyzation,winner


#tests to see if my calculate time actually works. Because a slower time is greater, a fast time should be lower than slower time.
def test_1():
    fast= Car("fast",10,5,5,5)
    slow = Car("slow",2,5,5,5)
    fast_time = calculate_time(fast,200,0,0)
    slow_time = calculate_time(slow,200,0,0)

    if slow_time<fast_time:
        print("Code failed")
    if fast_time<slow_time:
        print("Success")
#Winner returns the quickest car
def test_2():
    fast= Car("fast",10,5,5,5)
    slow = Car("slow",2,5,5,5)
    win_car, win_time = winner([fast,slow],200,0,0)
    if win_car.name == "fast":
        print("Success")

# A track that has no turns should return left_turns and right_turns ==0
def test_3():
    straight = [(0,0),(25,0),(50,0)]
    distance, left_turns, right_turns = track_analyzation(straight)
    assert round(distance,2)==50
    if left_turns==0 and right_turns==0:
        print ("Success")

test_1()
test_2()
test_3()

print ("All 3 tests passed")


