class Solution:
    def valid(self, checked: Counter, cnt: Counter) -> bool:
        for char, count in cnt.items():
            if checked[char] < count:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if not s or len(s) < len(t):
            return ""

        t_count = Counter(t)
        t_chars = set(t_count.keys())
        min_len = float('inf')
        result = ""

        left, right = 0, 0
        checked = Counter()
        
        while right < len(s):
            if s[right] in t_chars:
                checked[s[right]] += 1
                
            while self.valid(checked, t_count):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]
                
                if s[left] in t_chars:
                    checked[s[left]] -= 1
                    
                left += 1
                
            right += 1

        return result
