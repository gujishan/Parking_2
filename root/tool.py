# 统计数组信息
def all_list(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return result


# 删除数组中相同的元素
def zl_data(arr):
    zl = []
    for i in arr:
        if i not in zl:
            zl.append(i)
    return zl


# 分解年月日
def get_year(arr):
    year = arr.split('-', 2)[0]
    return year


def get_month(arr):
    month = arr.split('-', 2)[1]
    return month


def get_day(arr):
    day = arr.split('-', 2)[2]
    return day