import java.util.*;

class Solution {
    Map<String, Integer> eMap = new HashMap<>();
    Map<Integer, Integer> rMap = new HashMap<>();

    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        int[] money = new int[enroll.length];
        eMap.put("-", -1);
        for (int i = 0; i < enroll.length; i++) {
            String e = enroll[i];
            String r = referral[i];
            eMap.put(e, i);
            rMap.put(i, eMap.get(r));
        }

        for (int i = 0; i < seller.length; i++) {
            distribute(money, eMap.get(seller[i]), amount[i] * 100);
        }
        return money;
    }

    public void distribute(int[] money, int sellerId, int amount) {
        int upper = amount / 10;
        int mine = amount - upper;
        money[sellerId] += mine;
        int rid = rMap.get(sellerId);
        if (rid > -1 && upper > 0) {
            distribute(money, rid, upper);
        }
    }
}