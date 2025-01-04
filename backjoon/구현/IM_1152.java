package 구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class IM_1152 {
    private final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        String readLine = br.readLine().trim();
        if (readLine == ""){
            System.out.println(0);
            return;
        }
        String[] strings = readLine.split(" ");
        System.out.println(strings.length);
    }
}
