import math
import random
from typing import List, Tuple


def __linear_eq(maxval: int = 25, var_count: int = 2, add=True) -> List[int]:
    c = random.randint(5, maxval)
    while True:
        rand_n = [random.random() for _ in range(var_count)]
        result = [math.floor(i * c / sum(rand_n)) for i in rand_n]
        if 0 not in result:
            break
    for _ in range(c - sum(result)):
        result[random.randint(0, var_count - 1)] += 1
    if add:
        result.append(c)
    else:
        result.insert(0, c)
    return result


def __make_equation(vars_: List, mask_random: bool = False, op: str = "+") -> Tuple[str, str, str]:
    if mask_random:
        vars_[random.randint(0, len(vars_) - 1)] = "_"
    else:
        vars_[-1] = "_"
    s = op.join(str(i) for i in vars_[:-1])
    return s, "=", str(vars_[-1])


def generate_equation(var_count=2, max_val=25, mask_random=True, add=True) -> Tuple[str, str, str]:
    if add:
        return __make_equation(__linear_eq(maxval=max_val, var_count=var_count), mask_random=mask_random)
    return __make_equation(__linear_eq(maxval=max_val, var_count=var_count, add=False), mask_random=mask_random, op="-")


if __name__ == "__main__":
    for i in range(10):
        print(generate_equation(var_count=2, max_val=25, mask_random=True, add=True))
    for i in range(10):
        print(generate_equation(var_count=2, max_val=25, mask_random=True, add=False))
