# 모듈화 + 패키지 
#     + 모듈가져오기, 테스트 코드 배치 , 모듈가져오기 , 패키지 사용

# 모듈 
#    함수나 변수 또는 클래스를 모아 놓은 파일이다.
#     => 확장자가.py파일           
#     mod.py,__init__.py,p1.py, p2.py,...
 
# import 모듈이름
#  모듈이름.함수 모듈이름을 안쓰려면 -> from 모듈이름 import 모듈함수 
#  from mod1 import* -> * (모든것)을 의미 
# 모듈화의 대상 => 변수, 함수, 클래스 <= 요소를 가져다 내것 처럼 사용가능 

# 패키지  
#     유사한 기능 끼리 묶어둔 디렉토리 ,유틸리티 , 통신 , gui등등 모아둔것

# 패키지 폴더 내에 __init__.py 이 파일은 하위 호환을 위해서 python3.3이하에서는 모두 사용한다.
# 그리고, __init__.py는 곧 해당 패키지 자체를 의미한다


#-------------------------------
# from  패키지.패키지....모듈\ import 변수,함수,클레스(필요한것들 열거)
from a.b.mod import PI, add
print(PI)
print(add(1,2))

# from  패키지.패키지 \ import 변수, 함수, 클래스
# 경로상 마지막 패키지(디렉토리)안에 있는 __init__.py에서 모듈을 가져온다
from a.b import PI2 as pi2 # PI2 -> pi2 이름 변경 
print(pi2)

# 패키지명은 절대로 .들어가면 않된다!!
# 모듈명도 절대로 .들어가면 않된다!!
from a import PI3
print(PI3)

# 별칭 => 이름이 너무 길어서라든지, 이름 변경을 해서 사용하고 싶다면
# 원래이름 as 별칭
from a import PI3 as pi
print(pi)

# 가져올 모듈이 너무 많다. 다 가져왔으면 좋겟다 => *
# 하위 호환을 위해서는 
# __all__=['mod']
from a.b import *
print( mod.PI, PI2 )

# import만 사용시
import a.b.mod as m
print( m.PI )

import a.b as bm
print( bm.PI2 )

# 모듈을 가져온다는 것은 해당 모듈을 실행한다라고 봐도 무방하다->메모리 적제를 해야하니
# 내가 만든 모듈같은 경우 의도하지 않은 코드가 실행될수 있다
# => 테스트 할려고 만든 코드는 모듈 가져오기 수행시 실제로 구동되면 않된다
# => 이런 코드 처리가 필요하다 => __name__을 이용하여 처리 한다
# __name__을 사용하는 모듈을 직접 구동하면 "__main__"으로 나오고,
# 모듈로 사용되면(즉, 다른 모듀이 가져다 쓰면) "모듈명"으로 나온다

from Python08 import XMan
mu = XMan( '로건2', 100, 50, 51)
print( mu )
print('Python07 : __name__', __name__)