def centre_rect_x(rect1, rect2):
    return rect2[0] + (rect2[2] / 2) - (rect1[2] / 2)


def centre_text_x(label, rect):
    textPos = label.get_rect()
    textPos[0] = centre_rect_x(textPos, rect)
    return textPos[0]


