'''
https://stackoverflow.com/questions/48951591/python-find-longest-binary-gap-in-binary-representation-of-an-integer-number
'''

def binary_gap(N):
    return len(max(format(N, 'b').strip('0').split('1')))

print(binary_gap(5))