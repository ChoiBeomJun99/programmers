import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        List<Integer> completeDays = new ArrayList<>(); // 완료 날짜만을 보관하는 리스트
        
        for (int i = 0; i < progresses.length; i++) {
            int left = 100 - progresses[i];
            int x = left / speeds[i];
            
            if (left % speeds[i] != 0) {
                x ++;
            }
            
            completeDays.add(x);
        }
        
        // System.out.println(completeDays);
        Queue<Integer> queue = new LinkedList<>();
        
        for (int i = 0; i < completeDays.size(); i++) {
            int tmp = completeDays.get(i);
            
            if (queue.isEmpty()) {
                queue.add(tmp);
                continue;
            }
            
            if (queue.peek() < tmp) {
                answer.add(queue.size());
                queue.clear();
            }
            
            queue.add(tmp);
        }
        
        
        answer.add(queue.size());
        return answer.stream().mapToInt(x->x).toArray();
    }
}