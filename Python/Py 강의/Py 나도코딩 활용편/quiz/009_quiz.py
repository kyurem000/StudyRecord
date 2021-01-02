# 2020-06-22
# 001 ~ 008에서 배운 것을 이용하는 퀴즈 
# 하늘에서 떨어지는 똥 피하기 게임을 만드시오.

# [조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능 
# 2. 똥은 화면 가장 위에서 떨어짐, x좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. FPS는 30으로 고정 

# [게임 이미지]
# 1. 배경 : 640 * 480 - background.png
# 2. 캐릭터 : 70 * 70 - character.png
# 3. 똥 : 70 * 70 - enemy.png

#####################################################################
# 기본 초기화 ( 반드시 해야하는 것들 )
import pygame
import random

pygame.init() # 초기화 (반드시 필요함)

# 화면 크기 설정 
screen_width = 480 # 가로 크기  480
screen_height = 640 # 세로 크기 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("DDONG GAME") # 게임 이름 

# FPS [FPS]
clock = pygame.time.Clock()
#####################################################################

# 1.사용자 게임 초기화 ( 배경화면, 게임 이미지, 좌표, 속도, 폰트 등 설정하는 부분 )

# 배경만들기
background = pygame.image.load("C:\\Users\\hanapsk61\\Documents\\GitHub\\StudyRecord\\Py 나도코딩 활용편\\pygame_basic\\background2.png")

# 캐릭터 만들기
character = pygame.image.load("C:\\Users\\hanapsk61\\Documents\\GitHub\\StudyRecord\\Py 나도코딩 활용편\\pygame_basic\\character2.png")
character_size = character.get_rect().size
character_w = character_size[0]
character_h = character_size[1]
character_x_pos = (screen_width / 2) - (character_w / 2)
character_y_pos = screen_height - character_h

# 캐릭터 이동 위치 
to_x = 0
character_speed = 0.5

# 적(똥) 만들기
enemy = pygame.image.load("C:\\Users\\hanapsk61\\Documents\\GitHub\\StudyRecord\\Py 나도코딩 활용편\\pygame_basic\\ddong.png")
enemy_size = enemy.get_rect().size
enemy_w = enemy_size[0]
enemy_h = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_w)
enemy_y_pos = 0

# 적 이동 위치 
enemy_speed = 20

#  폰트 정의 
game_font = pygame.font.Font(None, 25) # 폰트 객체 생성 (폰트, 크기 )

text = game_font.render("timer: ",True,(255, 255, 255))
# 총 시간 
total_time = 10

# 시작 시간 정보 [텍스트]
start_ticks = pygame.time.get_ticks() # 현재 titck을 받아옴

# 이벤트 루프 
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임 수를 설정 
    print("FPS : " + str(clock.get_fps()))

    # 2. 이벤트 처리 (키보드,마우스 등 )
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
           running = False 

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            to_x -= character_speed
        elif event.key == pygame.K_RIGHT:
            to_x += character_speed

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_w:
        character_x_pos = screen_width - character_h

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_w)

    # 4. 충돌 처리 
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("==== 충돌했습니다. ====")
        running = False

    # 5. 화면에 그리기 
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(text,(10, 10))

    # 경과 시간 계산 
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 경과 시간을 1000으로 나누어서 초(s)단위로 표시 

    # render는 글자를 그리는 것 
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))

    # 시간, True, 글자 색상 
    screen.blit(timer,(60, 10)) # 남은 시간, 출력 위치 

    pygame.display.update()
    
pygame.guit()