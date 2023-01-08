import pygame
from pygame.locals import *
import random

# tham số hình dạng
size = width, height = (800, 800) # chiều rộng 800 chiều cao 800
road_w = int(width/1.6) #chiều rộng của đường đua 
roadmark_w = int(width/80) # chiều rộng của vạch kẻ đường 
# tham số vị trí
right_lane = width/2 + road_w/4 
left_lane = width/2 - road_w/4
# tham số hoạt hình
speed = 1    #tốc độ di chuyển của xe địch 

# initiallize the app
pygame.init()
running = True #tạo vòng lập cho game

# đặt kích thước xửa sổ
screen = pygame.display.set_mode(size)
# đặt tiêu đề cửa sổ
pygame.display.set_caption("@Minh Nhật car game")
# đặt màu nền cho cửa sổ
screen.fill((60, 220, 0))
# apply changes
pygame.display.update()

# tải xe mình
car = pygame.image.load("car.png")
#resize image
car_loc = car.get_rect()
car_loc.center = right_lane, height*0.8

# tải xe địch
car2 = pygame.image.load("otherCar.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height*0.2

counter = 0
# game loop
while running:
    counter += 1

    # tăng độ khó theo thời gian
    if counter == 5000:
        speed += 0.5  # đồ khó tăng lên 0.5
        counter = 0
        print("level up", speed)

    # xe địch di chuyển 
    car2_loc[1] += speed
    if car2_loc[1] > height:
        # ngẫu nhiên đặt lại tọa độ cho xe địch khi nó đi quá màn hình
        if random.randint(0,1) == 0:#Nó sẽ lấy số ngẫu nhiên từ 0 đến 1 
    #Nếu số ngẫu nhiên là 0, nó sẽ đặt tọa độ cho xe địch là tọa độ x của làn đường bên phải và tọa độ y là -200 (trên màn hình). 
            car2_loc.center = right_lane, -200
        else:
    #Nếu số ngẫu nhiên là 1, nó sẽ đặt tọa độ cho xe địch là tọa độ x của làn đường bên trái và tọa độ y là -200 (trên màn hình).
            car2_loc.center = left_lane, -200

    # end game logic
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:
        print("GAME OVER! YOU LOST!")
        break
    # Đoạn code "car2_loc[1] > car_loc[1] - 250" có nghĩa là tọa độ y của xe địch lớn hơn tọa độ y của xe người chơi trừ đi 250. 
    # Nó dùng để kiểm tra xem xe địch có đang ở phía trên xe người chơi hay không.
    #  Nếu tọa độ y của xe địch lớn hơn tọa độ y của xe người chơi trừ đi 250, thì điều kiện sẽ đúng. Nếu không, điều kiện sẽ sai.

    for event in pygame.event.get():
        if event.type == QUIT:
            # Nếu loại sự kiện là QUIT, nó sẽ gán running về False để kết thúc vòng lặp game. 
            running = False
        if event.type == KEYDOWN:
            #Nếu loại sự kiện là KEYDOWN, nó sẽ kiểm tra xem người chơi có bấm phím mũi tên trái hay phím A hay không. 
            #Nếu có, nó sẽ di chuyển xe người chơi sang trái. 
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2), 0])
            #Nếu người chơi bấm phím mũi tên phải hay phím D, nó sẽ di chuyển xe người chơi sang phải
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w/2), 0])
    
    # vẽ đường
    pygame.draw.rect(
        screen,#screen là đối tượng surface mà nó sẽ vẽ hình chữ nhật lên.
        (50, 50, 50),#màu xám
        (width/2-road_w/2, 0, road_w, height))#(width/2-road_w/2, 0, road_w, height) là tọa độ và kích thước của hình chữ nhật. Nó sẽ vẽ hình chữ nhật bắt đầu từ tọa độ (width/2-road_w/2, 0), có chiều rộng là road_w và chiều cao là height.
        # vẽ đường tâm
    pygame.draw.rect(
        screen,
        (255, 240, 60),#màu vàng nhạt
        (width/2 - roadmark_w/2, 0, roadmark_w, height))
    # # vẽ vạch kẻ đường bên trái 
    pygame.draw.rect(
        screen,
        (255, 255, 255),#màu trắng
        (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height))
    # # vẽ vạch kẻ đường bên phải
    pygame.draw.rect(
        screen,
        (255, 255, 255),#màu trắng
        (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height))

    # đặt hình ảnh ô tô trên màn hình
    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    # áp dụng các thay đổi
    pygame.display.update()

# thu gọn cửa sổ ứng dụng
pygame.quit()
