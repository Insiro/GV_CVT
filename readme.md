# GI_CVT

1. input 폴더 구성

    1. 대본 데이터를 input 폴더에 삽입  
       대본 데이터 : [Voice dataset of Genshin Impact](https://github.com/w4123/GenshinVoice)
    2. unpack.zip 수행후, input 폴더에 언어에 맞게 삽입  
       ![Alt text](document/folder.png)

2. config.json 수정

-   result.json을 참고하여 config.json 을 수정  
    |key|desc|
    |--|--|
    |From | 변환이 될 대상 음성의 정보 |
    |TO | 변환 목표의 정보|
    |mod| 변활이 될 음성의 경로|

3. wem Folder 구성
   변환할 모드를 wem 폴더에 압축해제

4. main.py 실행
