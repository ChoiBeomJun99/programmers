import java.util.*;

class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        ArrayList<Long> tmp = new ArrayList<Long>();
        
        for (long i = 1; i <= n; i ++) {
            tmp.add(i * x);
        }
        
        for (int i = 0; i < tmp.size(); i++) {
            answer[i] = tmp.get(i);
        }
    
        return answer;
    }
}