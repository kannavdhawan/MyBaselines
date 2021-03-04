# without sorting

def rankings(arr):
    ranking = [0] * len(arr)
    rank = 0
    maximum = max(arr)
    tracking = []
    while sum(arr) != (maximum + 1) * len(arr):
        minimum = min(arr)
        if minimum not in tracking:
            rank += 1
        ranking[arr.index(minimum)] = rank
        tracking.append(minimum)
        arr[arr.index(minimum)] = maximum + 1
    return ranking


arr = [25, 7, 54, 90, 7]
ranking = rankings(arr)
print(ranking)


