import pygame ,random, sys, time

# 定義顏色
background_color = pygame.Color(255, 255, 255) # 背景色為白色
snake_color = pygame.Color(0, 255, 0) # 蛇為綠色
food_color = pygame.Color(255, 0, 0) # 食物為紅色
bomb_color = pygame.Color(0, 0, 0) # 炸彈為黑色

# 初始化
pygame.init() # 初始化Pygame模組
screen = pygame.display.set_mode((1000, 600)) # 初始化視窗大小
pygame.display.set_caption("貪吃蛇") # 初始化視窗標題
map = [([0]*61) for i in range(101)] # 初始化地圖
snake_x = 10 # 初始化蛇的位置(x座標)
snake_y = 10 # 初始化蛇的位置(y座標)
food_x = random.randint(1, 100) # 初始化食物的位置(x座標)
food_y = random.randint(1, 60) # 初始化食物的位置(y座標)
snake_length = 5 # 初始化蛇的長度
way = 1 # 初始化蛇的前進方向
map[food_x][food_y] = -1

# 主程式循環
while True:
    screen.fill(background_color) # 初始化背景顏色
    time.sleep(0.1) # 延遲程序的執行(蛇的移動速度)

    # 監聽事件
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit() # 點擊關閉按鈕後退出程式
        
        # 監測鍵盤(以上下左右鍵操控並避免反向移動)
        elif(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_RIGHT) and (way != 2):
                way = 1
            elif(event.key == pygame.K_LEFT) and (way != 1):
                way = 2
            elif(event.key == pygame.K_UP) and (way != 4):
                way = 3
            elif(event.key == pygame.K_DOWN) and (way != 3):
                way = 4
    
    # 定義蛇移動方向
    if way == 1: 
        snake_x += 1 
    elif way == 2: 
        snake_x -= 1 
    elif way == 3: 
        snake_y -= 1 
    elif way == 4: 
        snake_y += 1
    
    if (snake_x >= 100) or (snake_y >= 60) or (snake_x < 0) or (snake_y < 0) or (map[snake_x][snake_y] > 0):
        sys.exit() # 判斷撞牆或碰到身體
    map[snake_x][snake_y] = snake_length

    # 繪製矩形
    for x, a1 in enumerate(map, 1):
        for y, a2 in enumerate(a1, 1):
            if(a2 > 0):
                map[x-1][y-1] = map[x-1][y-1]-1
                pygame.draw.rect(screen, snake_color, ((x-1)*10, (y-1)*10, 10, 10)) # 繪製蛇
            elif(a2 == -1):
                pygame.draw.rect(screen, food_color, ((x-1)*10, (y-1)*10, 10, 10)) # 繪製食物
    
    if(snake_x == food_x) and (snake_y == food_y):
        snake_length += 1 # 判斷蛇吃到食物
    
        # 食物消失後刷新食物
        while(map[food_x][food_y] != 0):
            food_x = random.randint(1, 100)
            food_y = random.randint(1, 60)
        map[food_x][food_y] = -1
    
    pygame.display.update()
