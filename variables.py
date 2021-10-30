import pygame
pygame.font.init()
FPS = 60
clock = pygame.time.Clock()
MENU_V = ['Play','Settings','Quit']
M_FONT = pygame.font.SysFont('Calibri', 40)
FONT = pygame.font.SysFont('Calibri', 35)
FONT2 = pygame.font.SysFont('Calibri', 60)
WHITE = (255,255,255)
BLACK = (0,0,0)
BG_COLOR = (255,213,213)
DIR = 'assets'
S_WIDTH  = 900
S_HEIGHT = 500
WIDTH = 40
HEIGHT = 150
BALL = pygame.image.load(f'{DIR}/ball.png')
LEFT_P = pygame.image.load(f'{DIR}/bat.png')
RIGHT_P = pygame.image.load(f'{DIR}/bat.png')
BALL = pygame.transform.scale(BALL,(50,50))
LEFT_P = pygame.transform.scale(LEFT_P,(WIDTH,HEIGHT))
RIGHT_P = pygame.transform.scale(RIGHT_P,(WIDTH,HEIGHT))
BORDER = pygame.Rect(S_WIDTH // 2, 0, 5,S_HEIGHT)
WINDOW = pygame.display.set_mode((S_WIDTH,S_HEIGHT))