from collections import defaultdict


def solution(genres, plays):
    answer = []
    
    hash_dict=defaultdict(list)
    
    for i in range(len(genres)):
        hash_dict[genres[i]].append((i,plays[i]))

    genre_total=[]
    
    #가장 많이 재생된 장르를 먼저 최대 2개까지 
    for key, val in hash_dict.items():
        # value에 해당하는 리스트를 내림차순으로 정렬
        # 파이썬의 sort()는 stable sort -> 장르번호 오름차순 정렬은 필요없음
        val.sort(key=lambda x:x[1],reverse=True)
        tmp_list=[x[1] for x in val]
        total=sum(tmp_list)
        
        # 장르별로 장르, 총합, 내림차순으로 정렬된 리스트 생성
        genre_total.append((key,total,val))
    
    
    genre_total.sort(key=lambda x:x[1],reverse=True)
    
    for key,total,val in genre_total:
        
        if len(val)<2:
            answer.append(val[0][0])
        else:
            answer.append(val[0][0])
            answer.append(val[1][0])
    
    return answer