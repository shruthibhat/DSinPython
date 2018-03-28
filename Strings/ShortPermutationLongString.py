"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
In other words, one of the first string's permutations is the substring of the second string.

"""

__author__ = "Shruthi"


class Solution(object):
    def check_in_long_string(self, s1, s2):
        """
        :param s1: String
        :param s2: String
        :return: boolean
        """

        if len(s1) > len(s2):
            return False

        s1map = []
        s2map = []

        for i in range(0, 26):
            s1map.insert(i, 0)
            s2map.insert(i, 0)

        # ord('a')  gives ascii value of a

        for i in range(0, (len(s1))):
            s1map[ord(s1[i]) - ord('a')] = s1map[ord(s1[i]) - ord('a')] + 1
            s2map[ord(s2[i]) - ord('a')] = s2map[ord(s2[i]) - ord('a')] + 1

        for i in range(0, (len(s2)-len(s1))):
            if self.__matches(s1map, s2map):
                return True
            s2map[ord(s2[i + len(s1)]) - ord('a')] = s2map[ord(s2[i + len(s1)]) - ord('a')] + 1
            temp = s2map[ord(s2[i]) - ord('a')]
            s2map[ord(s2[i]) - ord('a')] = temp - 1

        return self.__matches(s1map, s2map)

    def __matches(self, list1, list2):
        for i, item in enumerate(list1):
            if list1[i] != list2[i]:
                return False
        return True


if __name__ == "__main__":
    string1 = "ab"
    string2 = "eidbaooo"

    string3 = "ab"
    string4 = "eidboaoo"

    sol = Solution()
    print("Is string1 substring string2 ? :", sol.check_in_long_string(string1, string2))
    print("Is string3 substring string4 ? :", sol.check_in_long_string(string3, string4))