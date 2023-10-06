import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        Queue<Integer> queue = new LinkedList<>();
        
        // 큐에 넣어주기.
        for (int tmp : priorities) {
            queue.add(tmp);
        }
        
        int queueSize = queue.size();
        while (queueSize > 0) {            
            int max = Collections.max(queue);
            int tmp = queue.peek();
            
            if (max == tmp) {
                // 우선순위가 가장 높으므로, 뽑아서 실행해도 된다.
                queue.remove();
                queueSize --;
                answer ++; // 업무를 수행했으므로.
                
                if (location == 0) {
                    return answer;
                }
                
                location --;
            } else {
                // 우선순위가 안맞으므로, 다시 큐에 넣는다.
                queue.remove();
                queue.add(tmp);
                
                if (location == 0) {
                    location = queueSize - 1; // 큐 가장 뒤에 우리가 찾는 업무가 있다는 것
                } else {
                    // location은 계속해서 추적해주기
                    location --;
                }
            }
        }
        
        return answer;
    }
}