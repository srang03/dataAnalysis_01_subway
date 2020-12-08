# dataAnalysis_low project
## 파이썬을 활용한 데이터 분석 기본

[ data_practice ] 

파이썬 데이터 분석
### 1. 데이터 처리
1 파일 다루기
  + 01_getting_part_part_of_word.py
문자열로 이루어진 text 리스트에서 k로 시작하는 문자열을 하나씩 출력하는 print_korea() 함수를 작성한다.

+ 문자열 함수
  + 02_how_to_use_split.py
문자열을 리스트로 반환하는 split() 함수의 이해하기 위해 문자열 변수의 텍스트를 공백 기준으로 분리하고 리스트형으로 반환하는 break_into_words() 함수를 작성한다.

+ 리스트 함수
  + 03_how_to_use_append.py
리스트에서 b로 시작하는 요소를 새로운 리스트에 저장하는 make_new_list() 함수를 구현한다.

  + 04_how_to_use_upper_lower.py
리스트의 문자열 요소를 모두 소문자로 변환하는 lowercase_all_characters() 함수를 구현한다.

  + 05_how_to_use_replace.py
리스트의 문자열 요소에서 쉼표, 작은 따옴표, 느낌표를 제거하는 remove_special_characters() 함수를 작성한다.



### 2. 텍스트 파일 분석
1 파일 다루기
*06_file_open_read.py 
파일의 내용을 각 라인의 번호와 함께 출력하는 print_lines() 함수를 작성한다.

2 데이터 구조 다루기
*07_data_type_convert.py
data.txt 파일을 읽고 (단어, 빈도수) 튜플로 구성된 리스트를 반환하는 import_as_tuple() 함수를 구현한다.

*08_list_comprehension.py
단어 모음 words 리스트에서 prefix로 시작하는 단어만 리턴하는 filter_by_prefix 함수를 구현한다.

*09_data_sort.py
정렬의 기준에 대한 이해를 위해 get_freq()함수와 sort_by_frequency() 함수를 구현한다.

3 그래프 다루기
*10_graph_matplotlib.py
matplotlib 라이브러리를 활용하여 연도별 평균 기온 그래프를 그린다.

