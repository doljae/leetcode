#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        p_list = list(pattern)
        hash_map = {}
        booked = [0] * 26
        index = ord("a")

        if len(s_list) != len(p_list):
            return False

        for i in range(len(s_list)):
            if s_list[i] not in hash_map:
                if booked[ord(p_list[i]) - index]:
                    return False
                hash_map[s_list[i]] = p_list[i]
                booked[ord(p_list[i]) - index] = 1
            else:
                if hash_map[s_list[i]] != p_list[i]:
                    return False

        return True