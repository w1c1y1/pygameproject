from pygame import image, transform


def create_image(name, w, h):
    img = image.load(name)
    img = transform.scale(img, (w, h))
    return img
