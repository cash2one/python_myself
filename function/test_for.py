
def process_item(item):
    # setups
    # condition
    # processing
    # calculation
    return item + 1

item_list = [1,2,3]
results = [process_item(item) for item in item_list]

print results


# from itertools import accumulate
# a = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
# resutls = list(accumulate(a, max))