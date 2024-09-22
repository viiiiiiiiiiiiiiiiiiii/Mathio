def mean(data):
    return sum(data) / len(data)

def median(data):
    data.sort()
    n = len(data)
    mid = n // 2
    return (data[mid] + data[mid - 1]) / 2 if n % 2 == 0 else data[mid]

def mode(data):
    return max(set(data), key=data.count)

def standard_deviation(data):
    m = mean(data)
    return (sum((x - m) ** 2 for x in data) / len(data)) ** 0.5
