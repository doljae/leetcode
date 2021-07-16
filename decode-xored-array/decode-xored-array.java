class Solution {
        public int[] decode(int[] encoded, int first) {
            int[] answer = new int[encoded.length + 1];
            for (int i = 0; i < answer.length; i++) {
                if (i == 0) { answer[i] = first; } else {
                    answer[i] = answer[i - 1] ^ encoded[i - 1];
                }
            }
            return answer;
        }
    }