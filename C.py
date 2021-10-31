# 標準入力を受け付ける。
N, M = map(int, input().split())

next = 0
valid = True
for _ in range(N):
    B = list(map(int, input().split()))
    first = B[0]

    # ある行の先頭と次の行の先頭の数字に関して、確認する。((Bi, 0) + 7 == (Bi + 1, 0))
    if next != 0 and next != first:
        valid = False

    # 各行の先頭の数字をもとに、行の要素数の正しさを確認する。(各行の先頭の数字のidxを調べて、各行の要素数の長さと比較を行う。)
    idx = first % 7
    if idx == 0:
        row_len = 1
    else:
        row_len = 7 - idx + 1

    if row_len < len(B):
        valid = False

    # 各行に関して規則通りに並んでいるのか、確認する。((Bi, j+1) = (Bi, j) + 1になっているのか)
    row_check = first
    for j in range(1, len(B)):
        if row_check + 1 != B[j]:
            valid = False

        row_check = B[j]

    next = first + 7

if valid:
    print('Yes')
else:
    print('No')
