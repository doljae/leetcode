from collections import deque
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current_line = []
        words = deque(words)

        while words:
            current_word = words[0]

            if not current_line:
                current_line.append(words.popleft())
            else:
                line_length = sum(map(len, current_line))
                spaces = len(current_line)

                if line_length + spaces + len(current_word) > maxWidth:
                    result.append(current_line)
                    current_line = [words.popleft()]
                else:
                    current_line.append(words.popleft())

        result.append(current_line)

        justified_lines = []
        for line in result:
            used_length = sum(map(len, line))
            remaining_spaces = maxWidth - used_length
            justified_line = []

            if len(line) == 1:
                justified_lines.append("".join(line))
                continue

            equal_spaces, extra_spaces = divmod(remaining_spaces, len(line) - 1)

            for i, word in enumerate(line):
                justified_line.append(word)

                if i == len(line) - 1:
                    continue

                justified_line.append(" " * equal_spaces)

                if extra_spaces > 0:
                    justified_line.append(" ")
                    extra_spaces -= 1

            justified_lines.append("".join(justified_line))

        if justified_lines:
            last_line = justified_lines[-1]
            justified_lines.pop()
            justified_lines.append(" ".join(last_line.split()))

        return [line.ljust(maxWidth) for line in justified_lines]
