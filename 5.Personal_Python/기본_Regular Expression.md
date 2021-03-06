# 정규 표현식 - 패캠

## 정리해야함 
---

### 정규표현식을 숙지하고 커스텀 해보자 

---

## 정규표현식 Regular Expression

- **특정 패턴과 일치하는 문자열을 검색, 치환, 제거 하는 기능**      
    = > 특정 패턴을 찾는것           
    예를 들면 => 이메일 형식 판별, 전화번호 형식 판별, 숫자로만 이루어진 문자열 등

- raw string => 그대로 문자열로인식      

**문자열 앞에 r이 붙으면 해당 문자열이 구성된 그대로 문자열에 반환한다.** 

```py
# Raw string의 예
a = 'abcd\n hi' # escapce 문자열
print(a)
#  Raw string 이용 => 문자열 앞에 r이 붙임
b = r'abcd\n hi' 
print(b)
```
---

# 기본 패턴 
- 문자하나하나의 캐릭터(character)들은 정확히 해당 문자와 일치 
   - 패턴 test는 test 문자열과 일치
   - 대소문자의 경우 기본적으로 구별하나, 구별하지 않도록 설정 가능 
- 몇몇 문자들에 대해서 예외 존재 => 특별한의미로 사용 
   - . ^ $ * + ? { } [ ] \ | ( )
-  .(마침표) - 어떤 한개의 캐릭터(character)와 일치 
    - \w - 문자 character와 일치 [a-zA-Z0-9_]
    - \s - 공백문자와 일치
    - \t, \n, \r - tab, newline, return
    - \d - 숫자 character와 일치 [0-9]
    - ^ = 시작, $ = 끝 각각 문자열의 시작과 끝을 의미
    - \가 붙으면 스페셜한 의미가 없어짐. 예를들어 \\.는 .자체를 의미 \\\는 \를 의미
    - 자세한 내용은 [링크](https://docs.python.org/3/library/re.html) 참조
---

# search method
  - 첫번째로 패턴을 찾으면 match 객체를 반환
  - 패턴을 찾지 못하면 None 반환


  
```py
import re  # 정규식 패키지 

# search method
#  - 첫번째로 패턴을 찾으면 match 객체를 반환
#  - 패턴을 찾지 못하면 None 반환

# 패턴찾기 - 1
src_search = re.search(r'abc','abcdef')
print(src_search.start()) # 인덱스 번호 시작 0 
print(src_search.end()) # 인덱스 끝은 3 =>  3은 포함하지 않는다. 
idx = 'abcdef'
print(idx[3]) # d 
print(src_search.group()) # '그룹('abc')를 불러온다
print('='*50)

# 패턴 찾기 - 2 
src_search = re.search(r'abc','123abcdef')
print(src_search.start()) # 인덱스 번호 시작 3
print(src_search.end()) # 인덱스 끝은 6 =>  6은 포함하지 않는다. 
print(src_search.group()) # '그룹('abc')를 불러온다

# \d - 숫자 character와 일치 [0-9]
src_search = re.search(r'\d\d\d\w', '112abedwf119')
print(src_search) # match='112a'

# \w - 문자 character와 일치 [a-zA-Z0-9_]
# .. 은 어떠한 문자든지 2개가 앞에오고 문자를 출력하라 
src_search = re.search(r'..\w\w', '@#$%ABCDabcd')
print(src_search) #  match='$%AB'

# Meta-characters (메타 캐릭터)
# [ ] 문자들의 범위를 나타내기 위해서 사용함
# - [abck] : a or b or c or k
# - [abc.^] : a or b or c or . or ^
# - [a-d]  : -와 함께 사용되면 해당 문자 사이의 범위에 속하는 문자 중 하나
# - [0-9]  : 모든 숫자
# - [a-z]  : 모든 소문자
# - [A-Z]  : 모든 대문자
# - [a-zA-Z0-9] : 모든 알파벳 문자 및 숫자
# - [^0-9] : ^가 맨 앞에 사용 되는 경우 해당 문자 패턴이 아닌 것과 매
```