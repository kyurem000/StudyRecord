import pygame
# 탭과 스페이스바 혼용을 조심할 것 

pygame.init() # 초기화 (반드시 필요함)

# 화면 크기 설정 
screen_width = 480 # 가로 크기 
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 배경 이미지 불러오기 [배경]
background = pygame.image.load("C:\\Users\\hanapsk61\\Documents\\GitHub\\StudyRecord\\Py 나도코딩 활용편\\pygame_basic\\background.png")

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름 

# 이벤트 루프 
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 게임이 진행되고있는 동안 "어떠한 이벤트가 발생"하였는가  
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
           running = False # 게임이 진행중이 아님 

    # screen.fill((0, 0, 255)) # 파란색으로 배경색상 채우기 
    screen.blit(background,(0, 0)) # 배경 그리기 [배경] 맨왼쪽 맨위에 

    pygame.display.update()# 게임화면을 다시 그리기 [배경]
    
# 게임 종료
pygame.guit()