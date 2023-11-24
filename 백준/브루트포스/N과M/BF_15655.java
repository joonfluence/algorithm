package 브루트포스.N과M;

import java.util.Arrays;
import java.util.Scanner;

/*

https://www.acmicpc.net/problem/15654

4 2
9 8 7 1

*/
public class BF_15655 {
    private static int[] arr;
    private static int[] nums;
    private static boolean[] visited;
    private static int N, M;
    private static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        arr = new int[M];
        nums = new int[N];
        visited = new boolean[N];

        for (int i = 0; i < N; i++) {
            nums[i] = sc.nextInt();
        }

        Arrays.sort(nums);
        dfs(0,0);
        System.out.print(sb);
    }

    private static void dfs(int start, int depth){
        if(depth == M){
            for (int val: arr) {
                sb.append(val).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i = start; i < N; i++) {
            arr[depth] = nums[i];
            dfs(i+1, depth + 1);
        }
    }
}
