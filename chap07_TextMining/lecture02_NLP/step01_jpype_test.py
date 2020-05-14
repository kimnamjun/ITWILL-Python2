"""
JPype 설치하기
https://www.lfd.uci.edu/~gohlke/pythonlibs/
JPype 검색 후 Python 버전, 32 or 64 bit 맞게 whl 파일 다운로드
anaconda prompt 실행 후 'pip install [경로 + 파일 이름]' 입력
'Successfully installed JPype1-0.7.5' 확인
"""
import jpype
print(jpype.getDefaultJVMPath())  # C:\Program Files\Java\jre1.8.0_151\bin\server\jvm.dll