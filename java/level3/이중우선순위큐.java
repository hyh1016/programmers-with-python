import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        int[] answer = new int[2];
        TreeMap<Integer, Integer> pq = new TreeMap<>();
        for (String op: operations) {
            String[] inputs = op.split(" ");
            String cmd = inputs[0];
            int value = Integer.parseInt(inputs[1]);
            if (cmd.equals("I")) {
                int newValue = 1;
                if (pq.containsKey(value)) newValue = pq.get(value);
                pq.put(value, newValue);
            }
            else if (cmd.equals("D")) {
                if (pq.isEmpty()) continue;
                int k = 0;
                if (value == 1) k = pq.lastKey();
                else if (value == -1) k = pq.firstKey();
                int v = pq.get(k);
                if (v < 2) pq.remove(k);
                else pq.put(k, v-1);
            }
        }
        if (pq.isEmpty()) {
            answer[0] = 0;
            answer[1] = 0;
        }
        else {
            answer[0] = pq.lastKey();
            answer[1] = pq.firstKey();
        }
        return answer;
    }
}
