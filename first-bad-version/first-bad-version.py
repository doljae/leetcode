class Solution:
    def firstBadVersion(self, n):

        left, right = 0, n - 1

        while left <= right:
            # mid = (left + right) // 2
            mid = left + (right - left) // 2

            result = isBadVersion(mid)

            if result is False:
                left = mid + 1
            else:
                right = mid - 1

        return left