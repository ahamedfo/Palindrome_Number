class Solution(object):
    def isPalindrome(self, x):
        k = len(str(x))
        for first_idx, letter in enumerate(x):
            if str(x)[first_idx] != str(x)[k]:
                return False
            k -= 1
        return True

        """
        :type x: int
        :rtype: bool
        """
