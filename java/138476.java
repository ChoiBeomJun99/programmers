import java.util.*;

class Solution {    
    Map<Integer, Integer> map = new HashMap<>();
    
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        
        for(int e : tangerine) {
            map.put(e, map.getOrDefault(e, 0) + 1);
        }
        
        // map을 두 번째 요소 값으로 내림차순 정렬을 해준다.
        List <Integer> list = new ArrayList<>(map.keySet());
        list.sort((o1, o2) -> map.get(o2).compareTo(map.get(o1)));
            
        for (int tmp : list) {
            k -= map.get(tmp);
            answer ++;
            
            if (k <= 0) {
                break;
            }
        }
        
        return answer;
    }
}