class Solution {
    int[] twoSum(int[] numbers, int target) {
        int[] results = new int[2];
        int left = 0;
        int right = numbers.length - 1;

        while (left < right){
            int sum = numbers[left] + numbers[right];
            if (sum == target) {
                results[0] = left + 1;
                results[1] = right + 1;
                break;
            }
            else if (sum < target){
                left += 1;
            } else if (sum > target) {
                right -= 1;
            }
        }

        return results;
    }
}