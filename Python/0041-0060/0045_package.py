# 2020-06-17
# 패키지 : 하나의 디렉토리에 여러가지 모듈 파일을 갖다 놓은 것을 패키지라고 한다.
# __all__

# import travel.thailand # 주의할 점 : thailand 위치에는 여기는 항상 모듈이나 패키지"만" 가능하다. 클래스나 함수는 임포트를 직접 할 수 없다.
# trip_to = travel.thailand.ThaiLandPackage()
# trip_to.detail()


# from travel.thailand import ThaiLandPackage # from-import 구문에서는 가능하다. 타일랜드패키지라는 "클래스"를 불러온 것 
# trip_to = ThaiLandPackage()
# trip_to.detail()


# from travel import viet
# trip_to = viet.VietPackage()
# trip_to.detail()


# from travel import * # *을 쓰겠다는 것은 트라벨이란 패키지에 있는 모든 것을 가져오겠단 건데.. 실제로는 개발자가 문법상에서 공개범위를 설정해줘야한다.
# # 패키지안에 포함된것 중에서 임포트되길 원하는거만 공개를 하고 그외에는 비공개를 할 수 있다는 뜻 
# trip_to = viet.VietPackage()
# trip_to.detail()
# # __init__.py에서 
# __all__=["viet"] 를 적어주니 실행이 되는 것을 확인할 수 있다.


from travel import * 
trip_to = thailand.ThaiLandPackage() # __init__.py에 viet에 대해서만 공개를 한 상태라, 다른 것은 쓸 수 없으므로 수정을 해줘야한다.
trip_to.detail()
# __all__=["viet", "thailand"] 로 바꿔주니 실행이 되는 것을 확인할 수 있다.


# 모듈 위치 확인------------------------
import inspect
import random
print(inspect.getfile(random)) # random.py가 어느 위치에 있는지 표시해줌
print(inspect.getfile(thailand))