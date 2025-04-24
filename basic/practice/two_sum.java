import java.util.HashMap;

class Solution {
    public static int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap();
        for (int i = 0; i < nums.length; i++){
            int num = nums[i];
            int complement = target - num;
            if (map.containsKey(complement)) {
                int j = map.get(complement);
                return new int[] { j, i };
            }
            map.put(num, i);
        }

        return new int[]{};
    }
}