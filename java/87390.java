import java.util.*;

class Solution {
    public int[] solution(int n, long left, long right) {        
        int size = Long.valueOf(right - left + 1).intValue();
        int[] answer = new int[size];
                
        // int leftInt = Long.valueOf(left).intValue();
        // int rightInt = Long.valueOf(right).intValue();
        
        long tmp = Long.valueOf(n);
        int idx = 0;
        
        for (long i = left; i <= right; i++) {
            if (i / tmp > i % tmp) {
                answer[idx] = Long.valueOf(i / tmp + 1).intValue();
            } else {
                answer[idx] = Long.valueOf(i % tmp + 1).intValue();
            }
            idx ++;
        }
        
        return answer;
    }
}