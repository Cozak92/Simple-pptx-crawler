## Simple pptx crawler
---

몇 천장 분량의 pptx 파일 맞춤법 검사를 확인하기 위해 만들었습니다.

### 사용 언어
Python 3.7

### 사용 라이브러리
- [hanspell](https://github.com/ssut/py-hanspell#results) : 네이버 맞춤법 검사 지원 라이브러리
- [python-pptx](https://python-pptx.readthedocs.io/en/latest/index.html) : pptx 크롤링 라이브러리
- glob : 사용자가 제시한 조건에 맞는 파일명을 리스트 형식으로 반환
- re : 파이썬에서 정규 표현식을 지원하는 모듈