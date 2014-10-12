
def permute_by_range(digits):
    return ['{0:b}'.format(n).rjust(digits, '0')
            for n in range(2**digits)]

def permute_by_recursion(digits):
    if digits == 1:
        return ['0', '1']
    next = permute_by_recursion(digits-1)
    return ['0'+n for n in next] + ['1'+n for n in next]

def filter_x_recursively(x):
    for num, next in zip(x, x[1:]):
        if (num, next) == ('1','1'):
            return False
    return True

def filter_by_string_in(x):
    return '11' not in x

class Checker(object):
    def __init__(self, filter='string_in', permute='range'):
        self.permute = {
                'range': permute_by_range,
                'recurse': permute_by_recursion,
                }.get(permute)
        self.filter = {
                'string_in': filter_by_string_in,
                'recurse': filter_x_recursively,
                }.get(filter)

    def __call__(self, digits):
        permutations = self.permute(digits)
        filtered = filter(self.filter, permutations)
        return len(filtered)


