
# Django 기초

## 주차 학습
멋사 강의를 참고하여 열심히 수강해 주세요.
- [Class Lion (Django 오리엔테이션 ~ Model 실습)](https://classlion.net/)

### 참고할만한 사이트
내용이 부족하거나 더 공부하고 싶다면 아래 링크를 추천드려요.(선택사항)
- [7기 Django 교육자료 영상 스크립트 (BASIC 1-1. 기본환경 세팅하기~ BASIC 2-3. Word Counter 만들기 3)](https://www.notion.so/4eed5a2343bb4f09874fe6c56ea4ace8?v=138c8b8b488e42b6a2cc603714db9e4f)
- [장고걸스 튜토리얼](https://tutorial.djangogirls.org/ko/) 
- [점프 투 장고 교재 Wiki](https://wikidocs.net/book/4223)
- [Django 공식문서](https://docs.djangoproject.com/ko/3.1/)


## 주차 과제
1. 강의에서 진행하는 WordCount 과제를 완성해서 올려주세요.


2. 올라간 계산기 템플릿을 기반으로, 빈칸을 채워서 완성해주세요.
   -   채우실  내용은 주석 형태 (# 작성할 내용)로 적어놓았습니다. 관련 파일은 다음과 같습니다.
       -   example/settings.py, urls.py
       -   calculator/urls.py, views.py, models.py
       -   calculator/templates/calculator/mycalculator.html 파일입니다.
   -   메인화면에서는 User 모델을 저장합니다. (User모델은 name이라는 요소를 포함합니다.)
   -   Calculator는 자바스크립트가 포함되어, 코드를 전부 제공합니다. 혹시 관심이 있으시다면, 한번 스스로 만들어 보시는 것도 좋습니다. 
   -   Calculator 화면에서는 메인 화면에서 저장한 User의 name을 list 형태로 제시합니다. (해당 구성은 간단하게 model의 개념과 값을 가져오는 방법에 대해서 이야기 하기 위함입니다)
  
  
![메인페이지](mainPage.png)
![계산기페이지](calculatorPage.png)
    

### 제출방법 및 기한
팀별 레포지터리에 week2/이름 으로 폴더를 만들고(or 본인 브랜치에 week2 폴더를 만들고) 문제 풀이 코드를 **4월 27일 23:59**까지 업로드 해주세요. 
<br/>
이때, calculator 파일의 경우 .gitignore 파일을 꼭 넣어주세요. [생성할 수 있는 사이트](https://www.toptal.com/developers/gitignore)(venv등 다른 파일이 올라가는 것을 막기 위함입니다. django, venv 등을 추가해주세요. )
- ex) week2/남민정/wordcount, week2/남민정/calculator

