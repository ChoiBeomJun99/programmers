import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        Arrays.sort(people); // 오름차순 정렬
        int outPerson = 0; // 보트를 타고 나간 사람 수
        
        int minIdx = 0; // 가장 작은
        int maxIdx = people.length -1; // 가장 큰
        
        while (outPerson < people.length) {
            
            if (people[maxIdx] + people[minIdx] <= limit) {
                minIdx ++;
                maxIdx --;
                outPerson += 2;
            } else { 
                // 가장 무거운 사람만 빼기
                maxIdx --;
                outPerson += 1;
            }
            
            answer += 1;
        }
        
        return answer;
    }
}