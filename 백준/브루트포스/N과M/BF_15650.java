package 브루트포스.N과M;

import java.io.*;
import java.util.*;

/*

순열 https://www.acmicpc.net/problem/15650 https://st-lab.tistory.com/115

1. 숫자 조합을 입력 받는다.
2. 뽑아야 할 숫자를 계산한다.

 */
public class BF_15650 {

    public static int[] arr;
    public static boolean[] visited;
    public static int N, M;
    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        N = in.nextInt();
        M = in.nextInt();
        arr = new int[M];
        visited = new boolean[N];
        dfs(1, 0);
        System.out.println(sb);
    }

    static void dfs(int at, int depth){
        if (depth == M){
            for (int val: arr) {
                sb.append(val).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i = at; i <= N; i++) {
            arr[depth] = i;
            dfs(i+1, depth + 1);
        }
    }
}