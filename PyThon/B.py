# Pre, In, Post order task


def get_postorder(nnodes: int, preorder: str, inorder: str) -> str:
    postorder = ""
    root_idx = inorder.index(preorder[0])
    if root_idx:
        postorder += get_postorder(
            root_idx,
            preorder[1:],
            inorder
            )
    if root_idx != nnodes - 1:
        postorder += get_postorder(
            nnodes - root_idx - 1,
            preorder[root_idx + 1:],
            inorder[root_idx + 1:]
            )
    postorder += preorder[0]

    return postorder


ntests = int(input())

for _ in range(ntests):
    test_to_put = input().split()
    print(get_postorder(
        int(test_to_put[0]),
        test_to_put[1],
        test_to_put[2]
    ))


# test_len, test_pre, test_in = (5, "ABDEC", "DBEAC")
# print(get_postorder(test_len, test_pre, test_in))
