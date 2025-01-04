package 브루트포스.N과M;

import java.util.*;

/*

https://www.acmicpc.net/problem/15655

*/
public class BF_15655 {
    private static int[] arr;
    private static int[] nums;
    private static int N, M;
    private static ArrayList<String> results = new ArrayList<>();
    private static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        arr = new int[M];
        nums = new int[N];

        for (int i = 0; i < N; i++) {
            nums[i] = sc.nextInt();
        }

        Arrays.sort(nums);
        dfs(0);
        System.out.println(sb);
    }

    private static void dfs(int depth){
        if(depth == M){
            // n번
            for (int val: arr) {
                sb.append(val).append(" ");
            }
            sb.append("\n");
            return;
        }

        // n번
        int before = 0;
        for (int i = 0; i < N; i++) {
            if(before != nums[i]){
                before = nums[i];
                arr[depth] = nums[i];
                // n번
                dfs(depth + 1);
            }
        }
    }
}
