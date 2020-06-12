# 2020-06-12
# with 

# import pickle
# #  profile 파일을 열고 profile_file 이란 변수에 저장 
# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))
# # close 할 필요 없음 

# # 단 2줄로 파일 쓰기를 가능 
# with open("study.txt", "w", encoding="utf-8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

# # 단 2줄로 파일 읽기 가능 
with open("study.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read())