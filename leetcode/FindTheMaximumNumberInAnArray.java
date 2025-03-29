public class FindTheMaximumNumberInAnArray {
  public static int findMaximumInArray(int[] nums) {
    int maxNum = Integer.MIN_VALUE;
    for (int num : nums) {
      maxNum = Math.max(maxNum, num);
    }
    
    return maxNum;
  }
  
  public static void main(String[] args) {
    int[] nums = new int[] { 1, 3, 7, 0, 5};
    System.out.println(findMaximumInArray(nums));
  }
}
