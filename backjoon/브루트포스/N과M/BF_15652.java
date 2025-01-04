package 브루트포스.N과M;
import java.util.Scanner;

/*

각 정점에서 이동 가능한 정점들

1 - 1, 2, 3, 4
2 - 1, 2, 3, 4
3 - 1, 2, 3, 4
4 - 1, 2, 3, 4

 */

public class BF_15652 {

    private static int[] arr;
    private static int N, M;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        arr = new int[M];
        dfs( 1, 0);
    }

    private static void dfs(int start, int depth){
        if (depth == M){
            for (int val: arr) {
                System.out.print(val + " ");
            }
            System.out.println();
            return;
        }

        // 1부터 N까지 다시 탐색
        for (int i = start; i <= N; i++) {
            arr[depth] = i;
            dfs(i,depth + 1);
        }
    }
}
