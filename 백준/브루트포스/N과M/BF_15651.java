package 브루트포스.N과M;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/*

순열 https://www.acmicpc.net/problem/15651 https://st-lab.tistory.com/116

1. 숫자 조합을 입력 받는다.
2. 뽑아야 할 숫자를 계산한다.

 */
public class BF_15651 {

    private static int[] arr;
    private static int N, M;
    private static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        N = in.nextInt();
        M = in.nextInt();
        arr = new int[M];
        dfs(1,0);
        System.out.print(sb);
    }

    // at -> 출발 노드
    private static void dfs(int at, int depth) {
        // 깊이가 M이랑 같아지면 출력후 return
        if (depth == M) {
            for (int i = 0; i < M; i++) {
                sb.append(arr[i] + " ");
            }
            sb.append('\n');
            return;
        }

        // from -> 인접 노드 (n개)
        for (int i = at; i <= N; i++) {
            arr[depth] = i;
            dfs(i, depth + 1);
        }
    }
}

