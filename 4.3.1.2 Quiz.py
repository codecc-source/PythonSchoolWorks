import pygame, random

pygame.init()

bg = (0, 0, 0)
x = 600
y = 600
z = [x, y]

win = pygame.display

win.set_caption("Kermit")

surface = win.set_mode(z)

img1 = pygame.image.load('kermit.jpg')
img2 = pygame.image.load('kermit.jpg')
img3 = pygame.image.load('kermit.jpg')
img4 = pygame.image.load('kermit.jpg')
img5 = pygame.image.load('kermit.jpg')
img6 = pygame.image.load('kermit.jpg')
img7 = pygame.image.load('kermit.jpg')
img8 = pygame.image.load('kermit.jpg')
img9 = pygame.image.load('kermit.jpg')
img10 = pygame.image.load('kermit.jpg')

window = True

python_x1, python_y1 = 200,200
python_x2, python_y2 = 200,200
python_x3, python_y3 = 200,200
python_x4, python_y4 = 200,200
python_x5, python_y5 = 200,200
python_x6, python_y6 = 200,200
python_x7, python_y7 = 200,200
python_x8, python_y8 = 200,200
python_x9, python_y9 = 200,200
python_x10, python_y10 = 200,200

clock = pygame.time.Clock()

while window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window = False

    surface.fill(bg)

    surface.blit(img1, (python_x1, python_y1))
    surface.blit(img2, (python_x2, python_y2))
    surface.blit(img3, (python_x3, python_y3))
    surface.blit(img4, (python_x4, python_y4))
    surface.blit(img5, (python_x5, python_y5))
    surface.blit(img6, (python_x6, python_y6))
    surface.blit(img7, (python_x7, python_y7))
    surface.blit(img8, (python_x8, python_y8))
    surface.blit(img9, (python_x9, python_y9))
    surface.blit(img10, (python_x10, python_y10))

    if event.type:
        python_x1, python_y1 = random.randint(100, 500), random.randint(100, 700)
    if event.type:
        python_x2, python_y2 = random.randint(100, 500), random.randint(100, 700)
    if event.type:
        python_x3, python_y3 = random.randint(100, 500), random.randint(100, 700)
    if event.type:
        python_x4, python_y4 = random.randint(100, 500), random.randint(100, 700)
    if event.type:
        python_x5, python_y5 = random.randint(100, 500), random.randint(100, 700)
    if event.type:
        python_x6, python_y6 = random.randint(100, 500), random.randint(100, 700)
    if event.type:
        python_x7, python_y7 = random.randint(100, 500), random.randint(100, 700)
    if event.type:
        python_x8, python_y8 = random.randint(100, 500), random.randint(100, 700)
    if event.type:
        python_x9, python_y9 = random.randint(100, 500), random.randint(100, 700)
    if event.type:
        python_x10, python_y10 = random.randint(100, 500), random.randint(100, 700)

    win.update()
    clock.tick(20)

pygame.quit()