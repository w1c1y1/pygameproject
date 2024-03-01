from functions import image, levels, buttons, text, jump
import pygame.gfxdraw

pygame.init()


def draw_centered_text(txt, colour, font, y_coord, rect):
    label = font.render(txt, 1, colour)
    label_pos = [text.centre_text_x(label, rect), y_coord]
    screen.blit(label, label_pos)


def rect_to_rect_collision(a, b):
    leftSide = min(a[0], b[0])
    rightSide = max(a[0] + a[2], b[0] + b[2])
    if (rightSide - leftSide) < (
            a[2] + b[2]):
        topSide = min(a[1], b[1])
        bottomSide = max(a[1] + a[3], b[1] + b[3])
        if (bottomSide - topSide) < (a[3] + b[
            3]):
            return True


def point_inside_rectangle(a, b):
    if b[0] < a[0] < b[0] + b[2]:
        if b[1] < a[1] < b[1] + b[3]:
            return True


def colour_correction(rgb):
    if rgb[0] < 0:
        rgb[0] = 0
    elif rgb[0] > 255:
        rgb[0] = 255
    if rgb[1] < 0:
        rgb[1] = 0
    elif rgb[1] > 255:
        rgb[1] = 255
    if rgb[2] < 0:
        rgb[2] = 0
    elif rgb[2] > 255:
        rgb[2] = 255
    return rgb


def colour_changer(rgb, x):
    rgb[0] = rgb[0] + x
    rgb[1] = rgb[1] + x
    rgb[2] = rgb[2] + x
    rgb = colour_correction(rgb)
    return rgb


def escape_0(req, p):
    global escape
    if req:
        return escape
    else:
        escape = False
        click_sound.play()


def escape_1(req, p):
    global escape
    global scene
    if req:
        return escape
    else:
        escape = False
        scene = "main_menu"
        click_sound.play()


def main_menu_0(req, p):
    global scene
    if req:
        return scene == "main_menu"
    else:
        scene = "lvl_selection"
        click_sound.play()


def main_menu_1(req, p):
    global scene
    if req:
        return scene == "main_menu"
    else:
        scene = "instructions"
        click_sound.play()


def main_menu_2(req, p):
    global scene
    global done
    if req:
        return scene == "main_menu"
    else:
        done = True


def load_level(req, p):
    global scene
    if req:
        return scene == "lvl_selection"
    else:
        loadlevel(p)
        click_sound.play()


def back_arrow(req, p):
    global scene
    if req:
        return scene == "lvl_selection" or scene == "instructions"
    else:
        scene = "main_menu"
        click_sound.play()


def lvl_finish_0(req, p):
    global lvl_finish
    global scene
    if req:
        return lvl_finish is True
    else:
        lvl_finish = False
        scene = "main_menu"
        print("Returned to main menu")
        click_sound.play()


def lvl_finish_1(req, p):
    global lvl_finish
    if req:
        return lvl_finish is True
    else:
        lvl_finish = False
        currentLevel = scene[6:len(scene)]
        loadlevel(int(currentLevel))
        print("Replaying level")
        click_sound.play()


def lvl_finish_2(req, p):
    global lvl_finish
    global scene
    if req:
        return lvl_finish is True
    else:
        currentLevel = int(scene[6:len(scene)])
        if records[currentLevel] <= star_times[currentLevel][2]:
            lvl_finish = False
            if currentLevel < 9:
                loadlevel(currentLevel + 1)
            else:
                scene = "main_menu"
            print("Loaded next level")
        click_sound.play()


def loadlevel(n):
    if n == 0 or (records[n - 1] is not None and records[n - 1] <= star_times[n - 1][2]):
        print("Level " + str(n) + " was loaded.")
        reset_player()
        global lvl_start
        lvl_start = True
        global scene
        scene = "level_" + str(n)
        global boxes
        boxes = level[n]
        global lvl_timer
        lvl_timer = 0
        global lvl_timer_on
        lvl_timer_on = False


def reset_player():
    player[0] = size[0] / 2 - (player[2] / 2)
    player[1] = size[1] - 70 - player[3]
    player[2] = 50
    player[3] = 50
    vel[0] = 0
    vel[1] = 0


def submit_level_time(time, lvl):
    global records
    if records[lvl] is None or records[lvl] > time:
        records[lvl] = time


def draw_star(rect):
    global level_No
    global lvl_timer
    star_txt = ""
    if records[level_No] <= star_times[level_No][0]:
        screen.blit(gold_star_img, (text.centre_rect_x([0, 0, 128, 128], box), 280))
        star_txt = "You have recieved a Gold Star in this level!"
    elif records[level_No] <= star_times[level_No][1]:
        screen.blit(silver_star_img, (text.centre_rect_x([0, 0, 128, 128], box), 280))
        star_txt = "Score a time of at least " + str(
            round(star_times[level_No][0] / 1000, 3)) + " seconds to be awarded a Gold Star."
    elif records[level_No] <= star_times[level_No][2]:
        screen.blit(bronze_star_img, (text.centre_rect_x([0, 0, 128, 128], box), 280))
        star_txt = "Score a time of at least " + str(
            round(star_times[level_No][1] / 1000, 3)) + " seconds to be awarded a Silver Star."
    else:
        screen.blit(none_star_img, (text.centre_rect_x([0, 0, 128, 128], box), 280))
        star_txt = "Score a time of at least " + str(
            round(star_times[level_No][2] / 1000, 3)) + " seconds to be awarded a Bronze Star."
    draw_centered_text(star_txt, AQUA, font0, 440, rect)


def array_add(arr):
    n = 0
    for i in range(len(arr)):
        n += arr[i]
    return n


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
AQUA = (0, 255, 255)
PURPLE = (255, 0, 255)

size = (1080, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Super Meat Boy")
clock = pygame.time.Clock()
done = False

logo_img = image.create_image("images/gamelogo.png", 720, 260)
logo_img_pos = [text.centre_rect_x([0, 0, 720, 300], [0, 0, 1080, 720]), 0]
tile_img = image.create_image("images/grey_tile.png", 60, 60)
kill_img = image.create_image("images/kill.png", 60, 60)
finish_img = image.create_image("images/finish.png", 60, 60)
player_img = image.create_image("images/player.png", 50, 50)
background_img = image.create_image("images/cave_background.png", 1080, 720)
button_mainmenu_img = image.create_image("images/button_mainmenu.png", 100, 100)
button_replay_img = image.create_image("images/button_replay.png", 100, 100)
button_nextlvl_img = image.create_image("images/button_nextlvl.png", 100, 100)
button_back_img = image.create_image("images/button_back.png", 100, 50)

none_star_img = image.create_image("images/star_none.png", 128, 128)
bronze_star_img = image.create_image("images/star_bronze.png", 128, 128)
silver_star_img = image.create_image("images/star_silver.png", 128, 128)
gold_star_img = image.create_image("images/star_gold.png", 128, 128)
none_star_small_img = image.create_image("images/star_none.png", 50, 50)
bronze_star_small_img = image.create_image("images/star_bronze.png", 50, 50)
silver_star_small_img = image.create_image("images/star_silver.png", 50, 50)
gold_star_small_img = image.create_image("images/star_gold.png", 50, 50)
lock_small_img = image.create_image("images/lock.png", 50, 50)

font0 = pygame.font.Font(None, 36)
font1 = pygame.font.Font(None, 72)
font2 = pygame.font.Font(None, 90)
font3 = pygame.font.Font(None, 45)
font4 = pygame.font.Font(None, 60)

level_completed_txt = font2.render("Level Completed!", 1, AQUA)
level_completed_pos = [text.centre_text_x(level_completed_txt, [80, 80, 920, 560]), 110]

start_level_txt = font3.render("Press SPACEBAR to begin...", 1, AQUA)
start_level_pos = [text.centre_text_x(start_level_txt, [200, 475, 680, 150]), 575]

pygame.mixer.music.load('sound/background_music.wav')
pygame.mixer.music.play(-1)

jump_sound = pygame.mixer.Sound('sound/jump_effect.wav')
walljump_sound = pygame.mixer.Sound('sound/walljump_effect.wav')
doublejump_sound = pygame.mixer.Sound('sound/doublejump_effect.wav')
die_sound = pygame.mixer.Sound('sound/die_effect.wav')
click_sound = pygame.mixer.Sound('sound/click_effect.wav')
welcome_sound = pygame.mixer.Sound('sound/welcome_effect.wav')
levelcompleted_sound = pygame.mixer.Sound('sound/levelcompleted_effect.wav')

welcome_sound.play()

scene = "main_menu"
escape = False
pause = False
lvl_start = False
lvl_finish = False
lvl_timer_on = False
lvl_timer = 0

player = [0, 0, 50, 50, RED]
player[0] = size[0] / 2 - (player[2] / 2)
player[1] = size[1] - 70 - player[3]
vel = [0, 0]
playerSpeed = 8
playerJump = 6

GRAVITY = 13
FRICTION = 0.95

star_times = [
    [2850, 3100, 4000],
    [3600, 3900, 4800],
    [9700, 10500, 12000],
    [2650, 2800, 3500],
    [4300, 5350, 6500],
    [4800, 5400, 6300],
    [12000, 12500, 13300],
    [4000, 4500, 5300],
    [10000, 11000, 12500],
    [14500, 15200, 16100]]

level = levels.levels([[] for _ in range(
    10)])
level_No = 0
records = [None for _ in range(10)]

boxes = []

jumpAllowed = False
doubleJumpAllowed = False
doubleJump = False
inAir = True

moveUp = False
moveRight = False
moveLeft = False

mouseDown = False
buttons = buttons.create_buttons([])

print("Welcome to rectangle thingy with: ")
print("  - Left/Right Movement")
print("  - Jumping")
print("  - Gravity")
print("  - Collision with other rectangles")

while not done:
    mousePos = pygame.mouse.get_pos()
    if "level" in scene:
        level_No = int(scene[6:len(scene)])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moveUp = True
            elif event.key == pygame.K_RIGHT:
                moveRight = True
            elif event.key == pygame.K_LEFT:
                moveLeft = True
            elif event.key == pygame.K_ESCAPE:
                if escape:
                    escape = False
                    lvl_timer_on = True
                elif "level" in scene and not lvl_finish:
                    escape = True
                    lvl_timer_on = False
            elif event.key == pygame.K_SPACE:
                if lvl_start:
                    lvl_start = False
                    lvl_timer_on = True


            elif event.key == pygame.K_r:
                if lvl_finish_1(True, None):
                    lvl_finish_1(False, None)
                else:
                    loadlevel(level_No)


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                moveUp = False
            elif event.key == pygame.K_RIGHT:
                moveRight = False
            elif event.key == pygame.K_LEFT:
                moveLeft = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mouseDown == False:
                for i in range(len(buttons)):
                    if point_inside_rectangle(mousePos, buttons[i]):
                        if globals()[buttons[i][6]](True, buttons[i][7]):
                            buttons[i][5] = True
            mouseDown = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if mouseDown:
                for i in range(len(buttons)):
                    if point_inside_rectangle(mousePos, buttons[i]):
                        if buttons[i][5]:
                            if globals()[buttons[i][6]](True, buttons[i][7]):
                                print("Button " + str(buttons[i][6]) + " has been pressed", end="")
                                if buttons[i][7] is not None:
                                    print(" with parameter " + str(buttons[i][7]))
                                else:
                                    print("")
                                globals()[buttons[i][6]](False, buttons[i][7])
                    buttons[i][5] = False
            mouseDown = False

    if scene == "main_menu":
        screen.fill((127, 127, 127))
        screen.blit(logo_img, logo_img_pos)
        credits_txt = ""
        draw_centered_text(credits_txt, RED, font0, 680, [0, 0, 1080, 720])

    elif scene == "lvl_selection":
        screen.fill((127, 127, 127))
        renderText = "Aim for gold on all levels!"
        if records[len(records) - 1] is not None:
            renderText = "Time to complete all levels: " + str(array_add(records) / 1000) + " seconds"
        draw_centered_text(renderText, YELLOW, font4, 560, [0, 0, 1080, 720])

    elif scene == "instructions":
        screen.fill((127, 127, 127))
        instructions1_txt = "Instructions:"
        draw_centered_text(instructions1_txt, AQUA, font2, 60, [0, 0, 1080, 720])
        instructions2_txt = "Up arrow key to Jump"
        draw_centered_text(instructions2_txt, YELLOW, font3, 180, [0, 0, 1080, 720])
        instructions2_txt = "Left/Right arrow keys for left/right movement"
        draw_centered_text(instructions2_txt, YELLOW, font3, 230, [0, 0, 1080, 720])
        instructions2_txt = "ESCAPE to pause game AND/OR return to main menu"
        draw_centered_text(instructions2_txt, YELLOW, font3, 280, [0, 0, 1080, 720])

        instructions2_txt = "Go to this: "
        screen.blit(font3.render(instructions2_txt, 1, WHITE), (410, 380))
        screen.blit(kill_img, (600, 460))
        instructions2_txt = "Don't go to this: "
        screen.blit(font3.render(instructions2_txt, 1, WHITE), (332, 480))
        screen.blit(finish_img, (600, 360))

        instructions2_txt = "Be sure to utilise your ability to wall jump and double jump."
        draw_centered_text(instructions2_txt, GREEN, font3, 580, [0, 0, 1080, 720])
        instructions2_txt = "All done! Now go complete all the levels as fast as possible!"
        draw_centered_text(instructions2_txt, GREEN, font3, 640, [0, 0, 1080, 720])


    elif "level" in scene:
        if escape or lvl_start or lvl_finish:
            pause = True
        else:
            pause = False
        if not pause:
            if moveRight:
                if jump.player_jump_allowed(boxes, player):
                    vel[0] -= playerSpeed / 30
                else:
                    vel[0] -= playerSpeed / (30 * 2)
                if vel[0] < -playerSpeed:
                    vel[0] = -playerSpeed
            elif moveLeft:
                if jump.player_jump_allowed(boxes, player):
                    vel[0] += playerSpeed / 30
                else:
                    vel[0] += playerSpeed / (30 * 2)
                if vel[0] > playerSpeed:
                    vel[0] = playerSpeed

            jumpGround = jump.player_jump_allowed(boxes, player)
            jumpLeft = jump.player_left_wall_jump_allowed(boxes, player)
            jumpRight = jump.player_right_wall_jump_allowed(boxes, player)
            jumpAny = (jump.player_jump_allowed(boxes, player)
                       or jump.player_left_wall_jump_allowed(boxes, player)
                       or jump.player_right_wall_jump_allowed(boxes, player))

            if not inAir and not jumpAny:
                doubleJumpAllowed = True
            if jumpAny:
                inAir = False
            else:
                inAir = True
            if doubleJumpAllowed and not moveUp:
                doubleJumpAllowed = False
                doubleJump = True

            if not moveUp:
                if jumpAny:
                    jumpAllowed = True

            else:
                if jumpAllowed:
                    if jumpGround:
                        vel[1] = playerJump
                        jumpAllowed = False
                        jump_sound.play()
                    elif jumpLeft:
                        if vel[1] < 0:
                            vel[1] = playerJump
                            vel[0] = -2
                            jumpAllowed = False
                            walljump_sound.play()
                    elif jumpRight:
                        if vel[1] < 0:
                            vel[1] = playerJump
                            vel[0] = 2
                            jumpAllowed = False
                            walljump_sound.play()
                if doubleJump:
                    vel[1] = playerJump
                    doubleJump = False

            vel[1] -= GRAVITY / 60

            if not moveLeft and not moveRight and jump.player_jump_allowed(boxes,
                                                                           player):
                if vel[0] != 0:
                    vel[0] *= FRICTION
                if vel[0] < 1 / 60 and vel[
                    0] > -1 / 60:
                    vel[0] = 0

            player[0] -= vel[0]
            player[1] -= vel[1]

            for i in range(len(boxes)):
                if (boxes[i][5]):
                    if rect_to_rect_collision(player, boxes[i]):
                        N = player[1] + player[3] - boxes[i][1]
                        E = boxes[i][0] + boxes[i][2] - player[0]
                        S = boxes[i][1] + boxes[i][3] - player[1]
                        W = player[0] + player[2] - boxes[i][0]
                        if min(N, S, E, W) == N:
                            player[1] = boxes[i][1] - player[3]
                            if vel[1] < 0:
                                vel[1] = 0
                        elif min(E, S, W) == S:
                            player[1] = boxes[i][1] + boxes[i][3]
                            if vel[1] > 0:
                                vel[1] = 0
                            vel[0] *= 0.8
                        elif (E < W):
                            player[0] = boxes[i][0] + boxes[i][2]
                            if vel[0] > 0:
                                vel[0] = 0
                        else:
                            player[0] = boxes[i][0] - player[2]
                            if vel[0] < 0:
                                vel[0] = 0

                        if boxes[i][6] == "finish":
                            print("Level Completed")
                            levelcompleted_sound.play()
                            lvl_finish = True
                            lvl_timer_on = False
                            submit_level_time(int(lvl_timer), level_No)
                        elif boxes[i][6] == "kill":
                            print("Player Died")
                            die_sound.play()
                            loadlevel(level_No)

            if player[0] + player[2] < 0 or player[0] > size[0] or player[1] > size[1]:
                print("Player went outside the map.")
                die_sound.play()
                loadlevel(level_No)

        screen.fill(BLUE)
        screen.blit(background_img, (0, 0))

        for i in range(len(boxes)):
            pygame.draw.rect(screen, boxes[i][4], [boxes[i][0], boxes[i][1], boxes[i][2], boxes[i][3]])
            wR = boxes[i][2] / 60
            hR = boxes[i][3] / 60
            for w in range(int(wR)):
                for h in range(int(hR)):
                    if boxes[i][6] is None:
                        screen.blit(tile_img, (boxes[i][0] + (60 * w), boxes[i][1] + (60 * h)))
                    elif boxes[i][6] == "finish":
                        screen.blit(finish_img, (boxes[i][0] + (60 * w), boxes[i][1] + (60 * h)))
                    elif boxes[i][6] == "kill":
                        screen.blit(kill_img, (boxes[i][0] + (60 * w), boxes[i][1] + (60 * h)))

        screen.blit(player_img, (player[0], player[1]))

        if escape:
            MARGIN = 40
            pygame.gfxdraw.box(screen, pygame.Rect(MARGIN, MARGIN, size[0] - (2 * MARGIN), size[1] - (2 * MARGIN)),
                               (15, 15, 15, 191))

        if lvl_start:
            pygame.gfxdraw.box(screen, pygame.Rect(200, 475, 680, 150), (15, 15, 15, 191))
            screen.blit(start_level_txt, start_level_pos)
            level_txt = "Level " + str(level_No + 1)
            draw_centered_text(level_txt, AQUA, font1, 490, [200, 475, 680, 150])

        if lvl_finish:
            box = (80, 80, 920, 560)
            pygame.gfxdraw.box(screen, pygame.Rect(box), (15, 15, 15, 191))
            draw_star(box)
            screen.blit(level_completed_txt, level_completed_pos)
            timer_txt = "Time taken: " + str(lvl_timer / 1000) + " seconds"
            draw_centered_text(timer_txt, AQUA, font0, 200, box)
            record_txt = "Level record: " + str(records[level_No] / 1000) + " seconds"
            draw_centered_text(record_txt, AQUA, font0, 240, box)

    for i in range(len(buttons)):
        buttonColour = [buttons[i][4][0], buttons[i][4][1], buttons[i][4][2]]
        if buttons[i][5]:
            buttonColour = colour_changer(buttonColour, -63)
        if globals()[buttons[i][6]](True, buttons[i][7]):
            buttonRect = [buttons[i][0], buttons[i][1], buttons[i][2], buttons[i][3]]
            pygame.draw.rect(screen, buttonColour, buttonRect)
            if buttons[i][8] != None:
                screen.blit(buttons[i][8], (buttons[i][0], buttons[i][1]))
            if buttons[i][9] != None:
                draw_centered_text(buttons[i][9], BLUE, font1, buttons[i][1] + 20, buttonRect)

    if scene == "lvl_selection":
        for i in range(5):
            pos = [210 + (i * 175), 240]
            if records[i] is not None:
                if records[i] <= star_times[i][0]:
                    screen.blit(gold_star_small_img, pos)
                elif records[i] <= star_times[i][1]:
                    screen.blit(silver_star_small_img, pos)
                elif records[i] <= star_times[i][2]:
                    screen.blit(bronze_star_small_img, pos)
            else:
                if i != 0 and (records[i - 1] is None or records[i - 1] > star_times[i - 1][2]):
                    screen.blit(lock_small_img, pos)
        for i in range(5, 10):
            pos = [210 + ((i - 5) * 175), 410]
            if records[i] != None:
                if records[i] <= star_times[i][0]:
                    screen.blit(gold_star_small_img, pos)
                elif records[i] <= star_times[i][1]:
                    screen.blit(silver_star_small_img, pos)
                elif records[i] <= star_times[i][2]:
                    screen.blit(bronze_star_small_img, pos)
            else:
                if records[i - 1] == None or records[i - 1] > star_times[i - 1][2]:
                    screen.blit(lock_small_img, pos)

    if lvl_finish and records[level_No] > star_times[level_No][2]:
        screen.blit(lock_small_img, (745, 565))

    if "level" in scene:
        pygame.gfxdraw.box(screen, pygame.Rect(10, 5, 260, 36), (15, 15, 15, 127))
        lvl_timer_text = font0.render("Time: " + str(round(lvl_timer / 1000, 3)) + " seconds", 1, WHITE)
        screen.blit(lvl_timer_text, (20, 10))

    pygame.display.flip()
    if lvl_timer_on:
        lvl_timer += clock.get_time()
    clock.tick(60)

pygame.quit()
