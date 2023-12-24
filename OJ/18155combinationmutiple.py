from functools import lru_cache


@lru_cache(maxsize=None)
def achievable(t, nums):
    if t < min(nums, default=float('inf')):
        return False
    for i in range(len(nums)):
        if t == nums[i]: return True
        if t % nums[i] == 0 and achievable(t // nums[i], nums[:i] + nums[i + 1:]):
            return True
    return False


t, numbers = int(input()), tuple(map(int, input().split()))
print('YES' if achievable(t, numbers) else 'NO')
