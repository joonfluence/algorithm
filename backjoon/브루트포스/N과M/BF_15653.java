package 브루트포스.N과M;

import java.util.*;

/*

https://www.acmicpc.net/problem/15653

4 2
9 8 7 1

1. 정렬 : 1 7 8 9

1 -> 7
  -> 8
  -> 9
7 -> 1
  -> 8
  -> 9

*/
public class BF_15653 {
    private static int[] arr;
    private static int[] nums;
    private static boolean[] visited;
    private static ArrayList<String> results = new ArrayList<>();
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
        dfs(0);
    }

    private static void dfs(int depth){
        sb.setLength(0);
        if(depth == M){
            for (int val: arr) {
                sb.append(val).append(" ");
            }
            String string = sb.toString();
            if(!results.contains(string)){
                System.out.println(string);
                results.add(string);
            }
            return;
        }

        for (int i = 0; i < N; i++) {
            if(!visited[i]){
                visited[i] = true;
                arr[depth] = nums[i];
                dfs(depth + 1);
                visited[i] = false;
            }
        }
    }
}
