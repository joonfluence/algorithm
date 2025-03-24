public class MaximumAverageSubarray {
    public static double findMaxAverageBruteForce(int[] nums, int k) {
        double totalNum = Double.NEGATIVE_INFINITY;
        for (int i = 0; i < nums.length - k + 1; i++) {
            double totalNumInLoop = 0;
            for (int j = i; j < i+k; j++) {
                totalNumInLoop += nums[j];
            }

            totalNum = Math.max(totalNum, totalNumInLoop);
        }

        return totalNum / k;
    }
    public static double findMaxAverageSlidingWindow(int[] nums, int k) {
        double totalNum = 0;
        // 초기 합 초기화
        for (int i = 0; i < k; i++) {
            totalNum += nums[i];
        }

        double totalNumInLoop = totalNum;
        int idx = 0;
        while(idx < nums.length - k) {
            totalNumInLoop = totalNumInLoop - nums[idx] + nums[k + idx];
            totalNum = Math.max(totalNum, totalNumInLoop);
            idx += 1;
        }

        return totalNum / k;
    }

    public static void main(String[] args) {
        // int[] nums = new int[]{ -1 };
        int[] nums = new int[]{ 1,12,-5,-6,50,3 };
        // System.out.println(findMaxAverageBruteForce(nums, 1));
        System.out.println(findMaxAverageSlidingWindow(nums, 4));
    }
}
