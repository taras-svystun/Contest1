# BST task
from math import log2, floor


def BST_construct(nnodes, height, case_no):
    if height < floor(log2(nnodes)):
        return f"Case {case_no}: Impossible."
    return f"Case {case_no}: 1"

n, h = map(int, input().split())
case_num = 1
result = []

while n != 0 and h != 0:
    result.append(BST_construct(n, h, case_num))
    case_num += 1
    n, h = map(int, input().split())

print("\n".join(result))