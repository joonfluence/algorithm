class Solution {
    public static void moveZeroesBruteForce(int[] nums) {
        int insertIdx = -1;
        for (int i = 0; i < nums.length; i++) {
            // 값이 변경되어야 할 인덱스
            if (nums[i] == 0) {
                insertIdx = i;
            }

            // 0이 아닌 값을 찾아, 업데이트 한 후, 해당 값을 0으로 변경한다..
            for (int j = i; j < nums.length; j++) {
                if (insertIdx != -1 && nums[j] != 0) {
                    nums[insertIdx] = nums[j];
                    nums[j] = 0;
                    break;
                }
            }
        }
    }

    public static void moveZeroes(int[] nums) {
        int insertIdx = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                int originalNum = nums[insertIdx];
                nums[insertIdx] = nums[i];
                insertIdx++;
                if (originalNum == 0) {
                    nums[i] = 0;
                }
            }
        }
    }

    public static void main(String[] args) {
        int[] nums = new int[]{0, 1, 0, 3, 12};
        moveZeroes(nums);
    }
}