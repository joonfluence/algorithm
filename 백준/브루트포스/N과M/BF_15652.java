package 브루트포스.N과M;

import java.util.Scanner;

/*

순열

1. 숫자 조합을 입력 받는다.
2. 뽑아야 할 숫자를 계산한다.

 */
public class BF_15652 {

    public static int[] arr;
    public static int N, M;
    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        N = in.nextInt();
        M = in.nextInt();

        // 숫자 조합을 입력 받는다.
        int[] nums = new int[N];
        for (int i = 1; i <= N; i++) {
            nums[i-1] = i;
        }

        int[] output = new int[N];
        dfs(nums, output, 0, 0, N, M);
    }

    static void dfs(int[] arr, int[] output, int at, int depth, int n, int r){
        if (depth == r){
            print(output, r);
            return;
        }

        for (int i = at; i < n; i++) {
            output[depth] = arr[i];
            dfs(arr, output, i, depth+1, n, r);
        }
    }

    static void print(int[] arr, int r){
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < r; i++) {
            sb.append(arr[i]).append(" ");
        }
        System.out.println(sb);
    }
}

