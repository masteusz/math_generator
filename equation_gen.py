import math
import random
from typing import List, Tuple


def __linear_eq(maxval: int = 25, var_count: int = 2) -> List[int]:
    c = random.randint(5, maxval)
    rand_n = [random.random() for _ in range(var_count)]
    result = [math.floor(i * c / sum(rand_n)) for i in rand_n]
    for _ in range(c - sum(result)):
        result[random.randint(0, var_count - 1)] += 1
    result.append(c)
    return result


def __make_equation(vars_: List, mask_random: bool = False) -> Tuple[str, str, str]:
    if mask_random:
        vars_[random.randint(0, len(vars_) - 1)] = "_"
    else:
        vars_[-1] = "_"
    s = "+".join(str(i) for i in vars_[:-1])
    return s, "=", str(vars_[-1])


def generate_equation(var_count=2, max_val=25, mask_random=True) -> Tuple[str, str, str]:
    return __make_equation(__linear_eq(maxval=max_val, var_count=var_count), mask_random=mask_random)


if __name__ == "__main__":
    for i in range(10):
        print(__make_equation(__linear_eq(var_count=2), mask_random=False))
