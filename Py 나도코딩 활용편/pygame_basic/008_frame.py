# 2020-06-20
# 게임 개발 프레임

#####################################################################
# 기본 치기화 ( 반드시 해야하는 것들 )
import pygame
# 탭과 스페이스바 혼용을 조심할 것 

pygame.init() # 초기화 (반드시 필요함)

# 화면 크기 설정 
screen_width = 480 # 가로 크기 
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름 

# FPS [FPS]
clock = pygame.time.Clock()
#####################################################################

# 1.사용자 게임 초기화 ( 배경화면, 게임 이미지, 좌표, 속도, 폰트 등 설정하는 부분 )

# 이벤트 루프 
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정 
    print("FPS : " + str(clock.get_fps()))

    # 2. 이벤트 처리 (키보드,마우스 등 )
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
           running = False 

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리 
    
    # 5. 화면에 그리기 

    pygame.display.update()
    
pygame.guit()