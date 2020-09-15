# 0045와 같은 챕터 

class ThaiLandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 50만원")


# 모듈 직접 실행 
if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요.")
    trip_to = ThaiLandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")