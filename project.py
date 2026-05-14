import math
import pygame


from cars import Car, car1,car2,car3,car4


#all of the pygame functions were looked up as I wasn't very familiar with the external tool


def track_drawing_function():
    #Opens pygame and has it create a blank white screen where the user can draw the track. Pressing c clears the track and enter confirms the track. Returns the coordinates of points
    playing_game = True
    is_mouse_being_pressed = False
    track_points_pressed = []
    while playing_game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return track_points_pressed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                is_mouse_being_pressed = True
                track_points_pressed.append(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                is_mouse_being_pressed = False
            elif event.type == pygame.MOUSEMOTION and is_mouse_being_pressed:
                track_points_pressed.append(event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    track_points_pressed =[]
                elif event.key == pygame.K_RETURN:
                    return track_points_pressed
        screen_display.fill(white)

        if len(track_points_pressed) >= 2:
            pygame.draw.lines(screen_display,black,True,track_points_pressed,5)
        pygame.display.update()



def track_analyzation(when_pressed):
    # The calculation part of my code. Calculates the distance in pixels and the amount of left and right turns.
    track_distance=0
    track_left_turns=0
    track_right_turns=0

    for i in range(1,len(when_pressed)):
        x1,y1 = when_pressed[i-1]
        x2,y2 = when_pressed[i]
#looked up best ways to find distance
        distance_calc = math.sqrt((x2-x1)**2+(y2-y1)**2)
        track_distance += distance_calc
    for i in range(1, len(when_pressed)-1):
        x1,y1 = when_pressed[i-1]
        x2,y2 = when_pressed[i]
        x3,y3 = when_pressed[i+1]

        x_v1 = x2-x1
        y_v1 = y2-y1
        x_v2 = x3-x2
        y_v2 = y3-y2

        final_point_calc = (x_v1*y_v2)- (y_v1*x_v2)

        if final_point_calc >0:
            track_left_turns +=1
        elif final_point_calc <0:
            track_right_turns +=1
    return track_distance, track_left_turns, track_right_turns

def calculate_time(Car, track_distance, track_left_turns, track_right_turns):
    current_time=0
    current_time += track_distance/ Car.speed
    # The times 20 is to make it more even because before speeddemon was winning everytime
    current_time += (track_left_turns* 20)/Car.turn_left
    current_time += (track_right_turns* 20)/Car.turn_right
    current_time -= Car.distance

    return current_time

def winner(cars,track_distance, track_left_turns, track_right_turns):
    #Comapres the times of all the cars and returns the winner/fastest
    fastest_car=cars[0]
    fastest_time = calculate_time(fastest_car, track_distance, track_left_turns, track_right_turns)

    for car in cars:
        car_time = calculate_time(car, track_distance, track_left_turns, track_right_turns)
        print(car.name, "took", round(car_time,2), "seconds to finish")
        if car_time < fastest_time:
            fastest_time = car_time
            fastest_car = car

    return fastest_car, fastest_time
if __name__ == "__main__":
    pygame.init()

    width, height = 1000,700
    screen_display = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Draw your track here!")
    white = (255,255,255)
    black = (0,0,0)
    track = track_drawing_function()
    print("Tracking points:", track)
    track_distance, track_left_turns, track_right_turns = track_analyzation(track)

    print("Track distance", round(track_distance,2))
    print("Left Turns:", track_left_turns)
    print("Right Turns:", track_right_turns)

    cars = [car1,car2,car3,car4]

    winning_car, quickest_time = winner(cars, track_distance, track_left_turns, track_right_turns)

    print("the winner is:", winning_car.name)
    print("Winning time:", round(quickest_time,2),"seconds")


    pygame.quit()



    


