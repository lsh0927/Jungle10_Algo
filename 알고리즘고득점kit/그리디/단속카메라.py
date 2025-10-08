def solution(routes):
    # 진입 지점 기준으로 정렬
    routes.sort(key=lambda x: x[0])
    
    answer = 1  # 최소 1개는 필요
    camera = routes[0][1]  # 첫 차량의 진출 지점에 카메라
    
    for i in range(1, len(routes)):
        # 현재 차량이 카메라 범위 안에 있으면
        if routes[i][0] <= camera:
            # 겹치는 범위로 축소 (더 작은 끝점으로)
            camera = min(camera, routes[i][1])
        else:
            # 겹치지 않으면 새 카메라 필요
            answer += 1
            camera = routes[i][1]
    
    return answer