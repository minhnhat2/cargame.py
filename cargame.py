import pygame
from pygame.locals import *
import random

#tham số hình dạng
size = width, height = (800, 800)
road_w = int(width/1.6)
roadmark_w = int(width/80)
# tham số vị trí
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
# tham số hoạt hình
speed = 1

# khởi tạo ứng dụng
pygame.init()
running = True

# đặt kích thước cửa sổ
screen = pygame.display.set_mode(size)
# đặt tiêu đề cửa sổ
pygame.display.set_caption("Mariya's car game")

# load player vehicle
car = pygame.image.load("car1.png")
#thay đổi kích thước hình ảnh
car_loc = car.get_rect(center=(right_lane, height*0.8))

# tải xe địch
car2 = pygame.image.load("otherCar1.png")
car2_loc = car2.get_rect(center=(left_lane, height*0.2))

#khởi tạo điểm cao thành 0
high_score = 0

# khởi tạo phông chữ
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

counter = 0
# game loop
while running:
    counter += 1

    # tăng độ khó của trò chơi ngoài giờ
    if counter == 5000:
        speed += 0.5
        counter = 0
        print("level up", speed)

    # làm sinh động xe địch
    car2_loc[1] += speed
    if car2_loc[1] > height:
        # randomly select lane
        if random.randint(0,1) == 1:
            car2_loc.center = left_lane, -200
        else:
            car2_loc.center = right_lane, -200

    # end game logic
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:
        high_score = max(high_score, counter)
        print("GAME OVER! YOU LOST! Your Score : ",counter)
        print("High Score : ", high_score)
        running = False
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                running = True
                counter = 0
                car2_loc[1] = height*0.2
    screen.fill((60, 220, 0))
    replay_text = myfont.render('Replay', False, (0, 0, 0))
    replay_rect = replay_text.get_rect(center=(width / 2, height / 2))
    screen.blit(replay_text, replay_rect)
    
    # vẽ đường
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width/2-road_w/2, 0, road_w, height))
    #vẽ đường trung tâm
    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width/2 - roadmark_w/2, 0, roadmark_w, height))
    # vẽ vạch kẻ đường bên trái
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height))
    # vẽ vạch kẻ đường bên phải
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height))
    # đặt hình ảnh ô tô trên màn hình
    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    # áp dụng các thay đổi
    pygame.display.update()

    # event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            # di chuyển xe người dùng sang trái
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2), 0])
                if car_loc.centerx<=left_lane:
                    car_loc.centerx = left_lane
            # di chuyển xe của người dùng sang bên phải
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w/2), 0])
                if car_loc.centerx>=right_lane:
                    car_loc.centerx = right_lane
# thu gọn cửa sổ ứng dụng
pygame.quit()


