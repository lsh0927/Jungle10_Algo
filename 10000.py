class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        self.left = center - radius
        self.right = center + radius
        self.diameter = 2 * radius
        self.children = []
    
    def contains(self, other):
        # 완전히 내부에 포함 (접촉도 포함으로 간주)
        return (self.left <= other.left and other.right <= self.right and 
                self != other)
    
    def add_child(self, child):
        self.children.append(child)
    
    def get_children_diameter_sum(self):
        return sum(child.diameter for child in self.children)
    
    def calculate_regions(self):
        # 기본: 이 원 자체가 1개 영역
        regions = 1
        
        # 자식들의 영역을 재귀적으로 계산
        for child in self.children:
            regions += child.calculate_regions()
        
        # 자식들과 완전 접촉하면 추가 영역 +1
        if self.children and self.get_children_diameter_sum() == self.diameter:
            regions += 1
        
        return regions


def build_circle_tree(circles):
    # 반지름 큰 순으로 정렬
    circles.sort(key=lambda c: c.radius, reverse=True)
    roots = []
    
    for circle in circles:
        parent_found = False
        
        # 이 원을 포함할 수 있는 가장 작은 원 찾기
        for potential_parent in circles:
            if potential_parent.contains(circle):
                # 직접적인 부모인지 확인 (중간에 다른 원이 없는지)
                is_direct_parent = True
                for other in circles:
                    if (other != potential_parent and other != circle and
                        potential_parent.contains(other) and other.contains(circle)):
                        is_direct_parent = False
                        break
                
                if is_direct_parent:
                    potential_parent.add_child(circle)
                    parent_found = True
                    break
        
        if not parent_found:
            roots.append(circle)
    
    return roots


def solve():
    n = int(input())
    circles_data = []
    for _ in range(n):
        c, r = map(int, input().split())
        circles_data.append((c, r))
    
    if n == 0:
        return 1
    
    # Circle 객체 생성
    circles = [Circle(center, radius) for center, radius in circles_data]
    
    # 트리 구조 구축
    root_circles = build_circle_tree(circles)
    
    # 각 루트 트리의 영역 수 계산
    total_regions = 1  # 전체 평면의 기본 영역
    
    for root in root_circles:
        total_regions += root.calculate_regions()
    
    return total_regions

print(solve())