package 구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class IM_13410 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringBuilder tempStrings = new StringBuilder();
    private static ArrayList<Integer> resultArray = new ArrayList();

    public static void main(String[] args) throws IOException {
        Integer[] nums = Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt).toArray(Integer[]::new);
        int N = nums[0];
        int K = nums[1];
        int result;
        for (int i = 1; i <= K; i++) {
            result = N * i;
            char[] chars = String.valueOf(result).toCharArray();
            for (int j = chars.length; j > 0; j--) {
                tempStrings.append(chars[j-1]);
            }
            int parseInt = Integer.parseInt(String.valueOf(tempStrings));
            resultArray.add(parseInt);
            tempStrings.setLength(0);
        }

        System.out.println(resultArray.stream().sorted().toArray()[resultArray.size()-1]);
    }
}
