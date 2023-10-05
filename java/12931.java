import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        
        String tmp = Integer.toString(n);
        String[] N = tmp.split("");
        
        for (int i = 0; i < N.length; i++) {
            answer += Integer.parseInt(N[i]);
        }
        
        return answer;
    }
}