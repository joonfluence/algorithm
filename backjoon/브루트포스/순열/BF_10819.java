package 브루트포스.순열;

/*

6
20 1 15 8 4 10

*/

import java.util.Scanner;

public class BF_10819 {

    private static int N;
    private static int[] arr;
    private static int[] nums;
    private static boolean[] visited;
    private static Scanner sc = new Scanner(System.in);
    private static int result = Integer.MIN_VALUE;

    public static void main(String[] args) {
        // 갯수를 입력 받는다
        N = sc.nextInt();
        arr = new int[N];
        nums = new int[N];
        visited = new boolean[N];

        // 숫자를 입력 받는다
        for (int i = 0; i < N; i++) {
            nums[i] = sc.nextInt();
        }

        dfs(0);
        System.out.println(result);
    }

    private static void dfs(int depth) {
        if(depth == N){
            result = Math.max(getResult(), result);
            return;
        }

        // 인접한 노드
        for (int i = 1; i <= N; i++) {
            if(!visited[i-1]){
                visited[i-1] = true;
                arr[depth] = nums[i-1];
                dfs(depth+1);
                visited[i-1] = false;
            }
        }
    }

    public static int getResult(){
        int sum = 0;
        for (int i = 0; i < N-1; i++) {
            sum += Math.abs(arr[i] - arr[i+1]);
        }
        return sum;
    }
}
