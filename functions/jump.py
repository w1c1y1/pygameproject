def player_jump_allowed(boxes, player):
    for i in range(len(boxes)):
        if (max(player[0] + player[2], boxes[i][0] + boxes[i][2]) - min(player[0], boxes[i][0])) < (
                player[2] + boxes[i][2]):
            if (player[1] + player[3]) == boxes[i][1]:
                return True
    return False


def player_left_wall_jump_allowed(boxes, player):
    for i in range(len(boxes)):
        if boxes[i][6] is None:
            if (max(player[1] + player[3], boxes[i][1] + boxes[i][3]) - min(player[1], boxes[i][1])) < (
                    player[3] + boxes[i][3] + 10):
                if boxes[i][0] + boxes[i][2] <= player[0] < boxes[i][0] + boxes[i][2] + 10:
                    return True
    return False


def player_right_wall_jump_allowed(boxes, player):
    for i in range(len(boxes)):
        if boxes[i][6] is None:
            if (max(player[1] + player[3], boxes[i][1] + boxes[i][3]) - min(player[1], boxes[i][1])) < (
                    player[3] + boxes[i][3] + 10):
                if boxes[i][0] >= player[0] + player[2] > boxes[i][0] - 10:
                    return True
    return False
