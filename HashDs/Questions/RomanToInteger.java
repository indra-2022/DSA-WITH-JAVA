package HashDs.Questions;

import java.util.HashMap;

public class RomanToInteger {
    public static void main(String[] args) {
        RomanCheck("MCMXCIV");
    }

    public static void RomanCheck(String str) {
        int count = 0;
        HashMap<Character, Integer> map = new HashMap<>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);
        for (int i = 0; i < str.length()-1; i++) {
            char ch = str.charAt(i);
            char nxt = str.charAt(i + 1);
            if (map.get(ch) < map.get(nxt)) {
                count -= map.get(ch);
            } else {
                count += map.get(ch);
            }

        }
        count += map.get(str.charAt(str.length() - 1));
        System.out.println(count);

    }
}
