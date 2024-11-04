import sys
input = sys.stdin.readline

# 전위 순회 함수. 루트-왼-오
def preorder(node):
    if node == '.':  # 자식이 없을 때
        return ''

    for n in tree :
        if n[0] == node :
            left = n[1]
            right = n[2]
            break

    return node + preorder(left) + preorder(right)

# 중위 순회 함수. 왼-루트-오
def inorder(node):
    if node == '.':
        return ''

    for n in tree :
        if n[0] == node :
            left = n[1]
            right = n[2]
            break

    return inorder(left) + node + inorder(right)

# 후위 순회 함수. 왼-오-루트
def postorder(node):
    if node == '.':
        return ''

    for n in tree :
        if n[0] == node :
            left = n[1]
            right = n[2]
            break

    return postorder(left) + postorder(right) + node

n = int(input())  # 노드 개수
tree = []

for _ in range(n):
    node, left, right = input().split()
    tree.append([node, left, right])

print(preorder('A'))
print(inorder('A'))
print(postorder('A'))
