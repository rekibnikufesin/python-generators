#! /usr/bin/env python
"""
Python generator example
"""

"""Example function that can be replaced with a generator"""
# def countdown(num):
#     results = []
#     print('Starting')
#     while num > 0:
#         results.append(num)
#         num -= 1
#     return results

# launch_timer = countdown(5)
# print(launch_timer)

"""Generator that produces the same results"""
def countdown_gen(num):
    while num > 0:
        yield num
        num -= 1

launch_timer = countdown_gen(5)
for val in launch_timer:
    print(val)