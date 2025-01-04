package 구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class IM_10818 {
    private final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private final static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());
        Integer[] nums = Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt).toArray(Integer[]::new);
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;

        for (int i = 0; i < N; i++) {
            min = Math.min(min, nums[i]);
            max = Math.max(max, nums[i]);
        }

        sb.append(min);
        sb.append(" ");
        sb.append(max);
        System.out.println(sb);
    }
}
