import java.util.HashMap;

public class TwoSum {

    /**
     * nums : 배열 안에 숫자들 주어짐
     * target : 두 개의 숫자를 더해서 만들어 야 할 값
     **/
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            // 구해야 할 값
            int complement = target - nums[i];
            // 값이 있으면 map 에서 꺼내 쓰자
            if (map.containsKey(complement)){
                return new int[] { map.get(complement), i};
            } else {
                map.put(nums[i], i);
            }
        }
        return new int[0];
    }
}
