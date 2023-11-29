package 브루트포스.순열;

import java.io.IOException;
import java.util.Scanner;

/*

1. 순열로 목록을 계산한다.
2. 해당 목록을 구하기 위해

 */

public class BF_10974 {
    private static int N;
    private static int[] arr;
    private static boolean[] visited;
    private static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        arr = new int[N];
        visited = new boolean[N];
        dfs(1, 0);
        System.out.print(sb);
    }

    private static void dfs(int start, int depth){
        if(depth == N){
            for (int value: arr) {
                sb.append(value).append(" ");
            }
            sb.append("\n");
            return;
        }

        // 인접한 노드
        for (int i = 1; i <= N; i++) {
            if(!visited[i-1]){
                visited[i-1] = true;
                arr[depth] = i;
                dfs(i+1, depth+1);
                visited[i-1] = false;
            }
        }
    }
}
