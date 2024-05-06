import sys 
sys.path.append('../')
from utils import get_center_of_bbox, measure_distance

class PlayerBallAssigner():
    def __init__(self):
        #Max distance b/w player and the ball 
        self.max_player_ball_distance = 70
    
    #Used to mark the player who has the possesion of the ball at the moment.
    def assign_ball_to_player(self,players,ball_bbox):
        ball_position = get_center_of_bbox(ball_bbox)

        #Ball distance with the closest player in the frame
        miniumum_distance = 99999
        #Player who posseses the ball according to calculations
        assigned_player=-1

        #Looping over each player to get their tracking metrics
        for player_id, player in players.items():
            player_bbox = player['bbox']
            
            #Ball distance from left foot
            distance_left = measure_distance((player_bbox[0],player_bbox[-1]),ball_position)
            #Ball distance from the right foot
            distance_right = measure_distance((player_bbox[2],player_bbox[-1]),ball_position)
            distance = min(distance_left,distance_right)

            if distance < self.max_player_ball_distance:
                if distance < miniumum_distance:
                    miniumum_distance = distance
                    assigned_player = player_id

        return assigned_player