def quick_sort(a):
    if len(a) <= 1:
        return a
    q = a[0]
    left = [i for i in a if i < q]
    medium = [i for i in a if i == q]
    right = [i for i in a if i > q]
    return quick_sort(left) + medium + quick_sort(right)


def quick_sort_wo_memory(a, left, right):
    if left >= right:
        return
    pivotle = a[(left+right)//2]
    i, j = left, right
    while i <= j:
        while a[i] < pivotle: i += 1
        while a[j] > pivotle: j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i, j = i + 1, j - 1
    quick_sort_wo_memory(a, left, j)
    quick_sort_wo_memory(a, i, right)


def test_func():
    a = [5, 2, 4, 4, 1]
    a_sorted = [1, 2, 4, 4, 5]
    a_ans = quick_sort(a)
    print('zbs' if a_ans == a_sorted else '=(')
    quick_sort_wo_memory(a, 0, len(a) - 1)
    print('zbs' if a == a_sorted else '=(')


if __name__ == "__main__":
    test_func()
