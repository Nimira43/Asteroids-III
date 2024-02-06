import os

SCREENSIZE = (956, 560)
FONTPATH = os.path.join(os.getcwd(), 'assets/simkai.ttf')
IMAGEPATHS = {
    'asteroid': os.path.join(os.getcwd(), 'img/asteroid.png'),
    'bg_big': os.path.join(os.getcwd(), 'img/bg_big.png'),
    'bullet': os.path.join(os.getcwd(), 'img/bullet.png'),
    'seamless_space': os.path.join(os.getcwd(), 'img/seamless_space.png'),
    'ship': os.path.join(os.getcwd(), 'img/ship.png'),
    'ship_exploded': os.path.join(os.getcwd(), 'img/ship_exploded.png'),
    'space3': os.path.join(os.getcwd(), 'img/space3.jpg')
}
SOUNDPATHS = {
    'boom': os.path.join(os.getcwd(), 'assets/boom.wav'),
    'music': os.path.join(os.getcwd(), 'assets/music.mp3'),
    'shot': os.path.join(os.getcwd(), 'assets/shot.ogg')
}