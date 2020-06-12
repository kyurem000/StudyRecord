# 2020-06-12
# 파일입출력

# score_file = open("score.txt", "w", encoding="utf-8")
# # 위에서 w는 쓰기 용도, 덮어쓰기가 됨 
# print("수학 : 0", file=score_file)
# print("영어 : 50", File=score_file)
# score_file.close()
# 위 코드를 실행할 시 score.txt가 생기는 것을 볼 수 있다 


# score_file = open("score.txt", "a", encoding="utf-8")
# # 위에서 a는 업핸드를 뜻함. 파일을 이어서 쓸 수 있음 
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()
# # 위 코드를 실행할 시 "수학"과 "영어" 내용이 있던 파일에 "과학"과 "코딩" 점수를 추가한 것을 볼 수 있다 


# score_file = open("score.txt", "r", encoding="utf-8")
# # r은 read를 뜻함 읽어들임, 읽어들이는 방법도 여러가지가 있다 
# # .read()를 쓰면 한 번에 다 읽음 
# print(score_file.read())
# score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
# .readline을 이용하면 한 줄만 읽어들이고 커서는 다음 줄로 이동 
print(score_file.readline())
print(score_file.readline())
print(score_file.readline(),end="")
print(score_file.readline(),end="")
score_file.close()

# 만약에 줄바꿈을 안하고싶다면 readline()뒤에  ,end=""를 붙인다 