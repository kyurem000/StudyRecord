# 2020-06-12
# pickle : 프로그램 상에서 데이터를 파일형태로 저장해주는 것

import pickle
# profile_file = open("profile.pickle", "wb")
#     # 쓰기목적이기때문에 w를 적고 b는 바이너리를 의미 pickle을 쓰기위해선 항상 바이너리타입을 정리해주어야함 
#     # 인코딩은 따로 설정 안해도 됨  
# profile = {"이름":"박명수","나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile_file)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장 
# profile_file.close()

#  profile 이란 데이터를 pcikle을 이용해서 파일에 저장을 하고
# 그 파일에 있는 내용을 로드를 통해 불러와서 변수에 저장을해서 계속 쓸 수 있도록 도와주는 유용한 라이브러리 
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기 
print(profile)
profile_file.close()

