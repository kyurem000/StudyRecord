# 2020-06-17
# pip install

# 구글에서 pypi 에서 찾아보기 
# 패키지 설치 방법 :  cmd창으로 한다 (pip install ~~~)

# cmd창에 pip list 라고 적으면 현재 설치된 패키지를 보여준다.

# 패키지 삭제하는 방법 : pip uninstall 패키지명 

# 아래 구문은 beautifulsoup4이 설치되어있다면 실행, 아니라면 실행되지 않는다 
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print (soup.prettify())