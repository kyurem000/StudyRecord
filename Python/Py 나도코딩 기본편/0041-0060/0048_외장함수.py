# 2020-06-20
#외장함수 : 내장함수와는 다르게 직접 포트해서 사용해야하는 함수들

# list of python modules 검색 
# https://docs.python.org/ko/3/py-modindex.html
# 외장함수에 대해서 설명과 예제가 있다 

# # glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든 파일 

# # os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리를 표시 

# folder = "sample_dir"
# if os.path.exists(folder): 
#     print("이미지 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) # sample_dir이라는 폴더 생성 
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir())

# # time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는", datetime.date.today())

import datetime
# # timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜를 저장 
td = datetime.timedelta(days=100) # 100일 저장 
print("오늘부터 100일 후는", today + td) # 오늘부터 100일 후 