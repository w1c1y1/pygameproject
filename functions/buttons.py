from functions import image


def create_buttons(buttons):
    button_mainmenu_img = image.create_image("images/button_mainmenu.png", 100, 100)
    button_replay_img = image.create_image("images/button_replay.png", 100, 100)
    button_nextlvl_img = image.create_image("images/button_nextlvl.png", 100, 100)
    button_back_img = image.create_image("images/button_back.png", 100, 50)
    buttons.append(
        [340, 200, 400, 100, (200, 200, 200), False, "escape_0", None, None,
         "Return to Game"])
    buttons.append(
        [390, 400, 300, 100, (200, 200, 200), False, "escape_1", None, None, "Main Menu"])
    buttons.append([340, 300, 400, 100, (200, 200, 200), False, "main_menu_0", None, None,
                    "Select Level"])
    buttons.append([340, 425, 400, 100, (200, 200, 200), False, "main_menu_1", None, None,
                    "How to play"])
    buttons.append(
        [340, 550, 400, 100, (200, 200, 200), False, "main_menu_2", None, None,
         "Exit Game"])
    for i in range(5):
        buttons.append([140 + (175 * i), 170, 130, 130, (220, 220, 220), False, "load_level", i, None,
                        str(i + 1)])
    for i in range(5):
        buttons.append([140 + (175 * i), 340, 130, 130, (220, 220, 220), False, "load_level", i + 5, None,
                        str(i + 6)])
    buttons.append([50, 50, 100, 50, (200, 200, 200), False, "back_arrow", None, button_back_img,
                    None])

    buttons.append([300, 500, 100, 100, (200, 200, 200), False, "lvl_finish_0", None, button_mainmenu_img,
                    None])
    buttons.append([490, 500, 100, 100, (200, 200, 200), False, "lvl_finish_1", None, button_replay_img,
                    None])
    buttons.append([680, 500, 100, 100, (200, 200, 200), False, "lvl_finish_2", None, button_nextlvl_img,
                    None])
    return buttons
