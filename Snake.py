# 導入模組
import pygame ,random, sys, time

# 定義顏色
black = pygame.Color(0, 0, 0)
green = pygame.Color(0, 255, 0)
red = pygame.Color(255, 0, 0)
white = pygame.Color(255, 255, 255)

# 初始化
pygame.init() # 初始化Pygame模組
screen = pygame.display.set_mode((1000, 600)) # 初始化視窗大小
pygame.display.set_caption("貪吃蛇") # 初始化視窗標題
map = [([0]*61) for i in range(101)] # 初始化地圖
#初始化蛇的位置
snake_x = 10
snake_y = 10
snake_length = 5 # 初始化蛇的長度
way = 1 # 初始化蛇的前進方向
# 初始化食物的位置 random.randint(隨機最小值, 隨機最大值)
food_x = random.randint(7, 99)
food_y = random.randint(3, 59)
# 初始化炸彈的位置
bomb_x = random.randint(7, 98)
bomb_y = random.randint(3, 58)
# 初始化食物與炸彈在列表中的值
map[food_x][food_y] = -1
map[bomb_x][bomb_y] = -2 
score = 0 # 初始化分數

# 設定分數計算功能
def show_score():
	score_font = pygame.font.SysFont("times new roman", 20) # 設定字體與大小 score_font(字體, 字體大小)
	score_surface = score_font.render('Score : ' + str(score), True, white) # 建立顯示錶面對象 render(文字, 是否抗鋸齒, 顏色)
	score_rect = score_surface.get_rect() # 為文字表面物件建立一個矩形物件
	screen.blit(score_surface, score_rect) # 顯示文字

# 設定蛇的移動速度 time.sleep(延遲程式執行的秒數)
def snake_speed():
    if(score <= 2):
        time.sleep(0.1)
    elif(2 < score <= 4):
        time.sleep(0.09)
    elif(4 < score <= 6):
        time.sleep(0.08)
    elif(6 < score <= 8):
        time.sleep(0.07)
    elif(8 < score <= 10):
        time.sleep(0.06)
    elif(10 < score <= 12):
        time.sleep(0.05)
    elif(12 < score <= 14):
        time.sleep(0.04)
    elif(14 < score <= 16):
        time.sleep(0.03)
    elif(16 < score <= 18):
        time.sleep(0.02)
    elif(18 < score <= 20):
        time.sleep(0.01)
    else:
        time.sleep(0.001)

# 主程式循環
while True:
    screen.fill(black) # 初始化背景顏色
    snake_speed() # 
    # 監測事件 點擊關閉按鈕後關閉程式
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit()
        # 監測鍵盤 以上下左右鍵操控並避免反向移動
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
    # 判斷撞牆或碰到身體或碰到炸彈時關閉程式
    if (snake_x >= 100) or (snake_y >= 60) or (snake_x < 0) or (snake_y < 0):
        sys.exit() # 撞牆
    elif(map[snake_x][snake_y] > 0):
        sys.exit() # 碰到身體
    elif((snake_x == bomb_x) and (snake_y == bomb_y)) or ((snake_x == bomb_x+1) and (snake_y == bomb_y)) or ((snake_x == bomb_x) and (snake_y == bomb_y+1)) or ((snake_x == bomb_x+1) and (snake_y == bomb_y+1)):
        sys.exit() # 碰到炸彈
    map[snake_x][snake_y] = snake_length # 儲存蛇在列表中的長度
    # 繪製矩形
    # for 位置, 索引值 in enumerate(列表, 位置起始值) 
    for x, a1 in enumerate(map, 1):
        for y, a2 in enumerate(a1, 1):
            # pygame.draw.rect(畫布, 顏色, (x座標, y座標, 寬度, 長度))
            if(a2 > 0):
                map[x-1][y-1] = map[x-1][y-1]-1
                pygame.draw.rect(screen, green, ((x-1)*10, (y-1)*10, 10, 10)) # 繪製蛇
            elif(a2 == -1):
                pygame.draw.rect(screen, red, ((x-1)*10, (y-1)*10, 10, 10)) # 繪製食物
            elif(a2 == -2):
                pygame.draw.rect(screen, white, ((x-1)*10, (y-1)*10, 20, 20)) # 繪製炸彈
    # 判斷蛇吃到食物
    if(snake_x == food_x) and (snake_y == food_y):
        snake_length += 1
        score += 1
        # 刷新炸彈
        map[bomb_x][bomb_y] = 0
        bomb_x = random.randint(7, 98)
        bomb_y = random.randint(3, 58)
        # 食物消失後刷新食物與炸彈，直到不會與其他物體重疊
        while(map[food_x][food_y] != 0):
            food_x = random.randint(7, 99)
            food_y = random.randint(3, 59)
        while(map[bomb_x][bomb_y] != 0):
            bomb_x = random.randint(7, 98)
            bomb_y = random.randint(3, 58)
        # 重置食物與炸彈在列表中的值
        map[food_x][food_y] = -1
        map[bomb_x][bomb_y] = -2
    show_score() # 顯示分數
    pygame.display.update() #更新畫面
