import java.util.*;

class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "Yes";
        
        // 두 개의 카드를 큐로 구현
        Queue<String> queue1 = new LinkedList<>(Arrays.asList(cards1));
        Queue<String> queue2 = new LinkedList<>(Arrays.asList(cards2));
                
        for (int i = 0; i < goal.length; i++) {    
            String tmp = goal[i];
            
            if (!queue1.isEmpty() && queue1.peek().equals(tmp)) {
                queue1.remove();
            } else if (!queue2.isEmpty() && queue2.peek().equals(tmp)) {
                queue2.remove();
            } else {
                return "No";
            }
        }
        
        return answer;
    }
}