import java.util.*;

class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        Set<Integer> right = new HashSet<>();
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int t : topping) {
            right.add(t);
            map.put(t, map.getOrDefault(t, 0) + 1);
        }

        Set<Integer> left = new HashSet<>();
        for (int i = 0; i < topping.length; i++) {
            int t = topping[i];
            left.add(t);
            int count = map.get(t);
            if (count == 1) {
                map.remove(t);
                right.remove(t);
            } else {
                map.put(t, map.get(t) - 1);
            }
            if (left.size() == right.size())
                answer++;
        }
        return answer;
    }
}
