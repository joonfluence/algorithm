package 구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class IM_2739 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringBuffer sb = new StringBuffer();
    public static void main(String[] args) throws IOException {
        String line = br.readLine();
        int N = Integer.parseInt(line);
        for (int i = 1; i <= 9; i++) {
            sb.append(N);
            sb.append(" * ");
            sb.append(i);
            sb.append(" = ");
            sb.append(N * i);
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
