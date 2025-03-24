import java.util.HashMap;

class Solution {
  public boolean containsDuplicate(int[] nums) {
      HashMap<Integer, Boolean> hasNumberMap = new HashMap<>();

      for(int num : nums){
          if (hasNumberMap.containsKey(num)){
              return true;
          }

          hasNumberMap.put(num, true);
      }

      return false;
  }
}