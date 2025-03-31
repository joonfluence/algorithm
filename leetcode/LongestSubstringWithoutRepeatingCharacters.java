class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> seen = new HashSet<>();
        int left = 0, maxLen = 0;

        for (int right = 0; right < s.length(); right++){
            char c = s.charAt(right);

            // 중복된 값이 있으면 계속 제거해준다 
            while (seen.contains(c)){
                seen.remove(s.charAt(left));
                left++;
            }

            seen.add(c);
            maxLen = Math.max(maxLen, right - left + 1);
        }
        
        return maxLen;
    }
}