package 브루트포스.순열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*

https://dundung.tistory.com/58

 */

public class BF_10973 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringBuilder sb = new StringBuilder();
    private static int N;
    private static int[] nums;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        nums = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        if (nextPerm()){
            for (int val: nums) {
                sb.append(val).append(" ");
            }
        } else {
            sb.append("-1");
        }
        System.out.println(sb);
    }

    private static boolean nextPerm(){
        int size = nums.length - 1;
        int i = size;
        while (i > 0 && nums[i-1] <= nums[i]){
            i -= 1;
        }

        // 첫 번째 순열인 경우
        if(i <= 0){
            return false;
        }

        // nums[i-1] > nums[j]를 만족하는 첫 번째 수 찾기
        int j = size;
        while (nums[j] >= nums[i-1]){
            j -= 1;
        }

        // nums[i-1]와 nums[j]를 swap
        swap(i-1, j);
        j = size;

        // i부터 a.length-1까지 순열 뒤집기
        while (i < j){
            swap(i, j);
            i += 1;
            j -= 1;
        }

        return true;
    }

    private static void swap(int i, int j) {
        int temp = nums[j];
        nums[j] = nums[i];
        nums[i] = temp;
    }
}
