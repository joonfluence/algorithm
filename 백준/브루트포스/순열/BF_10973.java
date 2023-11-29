package 브루트포스.순열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*

https://zzingonglog.tistory.com/18

1. A[i-1] < A [i]를 만족하는 가장 큰 i를 찾는다.
2. j >= i 이면서 A[j] > A [i-1]을 만족하는 가장 큰 j를 찾는다.
3. A[i-1]과 A [j]를 swap 한다.
4. A[i] 부터 순열을 뒤집는다.

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

        if(i <= 0){
            return false;
        }

        int j = size;

        while (nums[i-1] >= nums[j]){
            j -= 1;
        }

        swap(i-1, j);
        j = size;

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
