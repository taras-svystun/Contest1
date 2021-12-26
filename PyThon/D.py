# Ski track task

distance = int(input())
road = list(map(int, input().split()))
"""
def maximal_track(track: list, to_match=0) -> int:
    max_len = 0
    straight, reverse = 0, 0
    temp_s, temp_r = 0, 0
    for area in track:
        if area:
            straight += 1
            temp_s += 1
        else:
            straight -= 1
            temp_s += 1
        if not straight:
            max_len = temp_s

    for area in track[::-1]:
        if area:
            reverse += 1
            temp_r += 1
        else:
            reverse -= 1
            temp_r += 1
        if not reverse:
            max_len = temp_r

    return max_len


def maximal_track2(track: list) -> int:
    max_len = 0
    idx = 0

    while idx < len(track):
        temp_max = 0
        counter = 0
        for area in track[idx:]:
            if area:
                counter += 1
            else:
                counter -= 1
            temp_max += 1
            if not counter and temp_max > max_len:
                max_len = temp_max
        idx += max(1, counter)

    return max_len
"""

def maximal_track3(track: list, length: int) -> int:
    remain = {0: -1}
    max_len = 0
    to_match = 0
    idx = 0
    while idx < length:
        if track[idx]:
            to_match += 1
        else:
            to_match -= 1

        if to_match in remain:
            max_len = max(idx - remain[to_match], max_len)
        else:
            remain[to_match] = idx
        idx += 1
    return max_len

# test = [1, 1, 1, 0, 0, 0]
print(maximal_track3(road, distance))
