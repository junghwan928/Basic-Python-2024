# file : test12_dictionary.py
# desc : 복합자료형 딕셔너리 

## 사전형 = key와 value 쌍을 나열해 놓은 자료형 
# { key : value , key : value , key : value, ....}
dict_movie = {'name': '어벤져스 엔드게임','type': '히어로 무비' , 
              'year' : 2019 , 'director':['안소니 루소', '조 루소'],
              'cast' : ['아이언맨' , '타노스' , '헐크' , '토르' , '닥터스트레인지']}




print(dict_movie['name'])
print(dict_movie['year'])

dict_movie['year']=2020
print(dict_movie)

dict_movie['producer'] = '케빈 파이기'
print(dict_movie)

print(dict_movie['producer'])

if 'producer' in dict_movie:  #딕셔너리에 키가 있는지 확인할때
    print(dict_movie['producer'])
else:
    print('제작자 없음')

musician = dict_movie.get('musician')
print('반복문---------------------------------')
#print(dict_movie['musician']) #오류(예외) 발생

#반복문으로 출력 
for key , value in dict_movie.items():
    print(key , ':' , dict_movie[key])