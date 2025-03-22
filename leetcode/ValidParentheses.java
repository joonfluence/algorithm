import java.util.HashMap;
import java.util.Stack;

public class ValidParentheses {
    class Solution {
        public boolean isValid(String s) {
            Stack<String> stack = new Stack<>();
            HashMap<String, Integer> map = new HashMap<>();

            map.put("[", 1);
            map.put("]", 1);
            map.put("{", 2);
            map.put("}", 2);
            map.put("(", 3);
            map.put(")", 3);

            // String 문자열 각각을 한글자 단위로 변환한다.
            String[] word = s.split("");
            for (String letter : word){
                if (letter.equals("[") || letter.equals("(") || letter.equals("{")){
                    stack.push(letter);
                } else {
                    if (!stack.isEmpty() && map.get(letter) == map.get(stack.peek())){
                        stack.pop();
                    } else {
                        return false;
                    }
                }
            }

            return stack.isEmpty();
        }
    }
}
