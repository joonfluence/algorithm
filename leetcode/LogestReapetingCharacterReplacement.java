class Solution {
  public int characterReplacement(String s, int k) {
      int[] freq = new int[26]; // A~Z 개수 추적
      int left = 0, maxCount = 0, maxLen = 0;

      for (int right = 0; right < s.length(); right++){
          char c = s.charAt(right);
          freq[c - 'A']++;
          maxCount = Math.max(maxCount, freq[c - 'A']);
          
          if ((right - left + 1) - maxCount > k){
              freq[s.charAt(left) - 'A']--;
              left++;
          }

          maxLen = Math.max(maxLen, right - left + 1);
      }

      return maxLen;
  }
}