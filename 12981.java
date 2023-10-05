import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = {0 ,0};
        
        List<String> sayWords = new ArrayList<String>();
        
        // 현재 끝말 잇기하는 사람의 번호
        int personNumber = 1;
        int turnCount = 1;
        
        // 끝말잇기 진행
        for(int i = 0; i < words.length; i++) {
            // 끝말잇기 여부 확인
            if ( i > 0 ) {
                String prev = words[i-1];
                String now = words[i];
                
                if (prev.charAt(prev.length() - 1) != now.charAt(0)) {
                    int[] tmp = {personNumber, turnCount};
                    return tmp;    
                }
                
            }
                
            // 이미 말한 단어인지 체크하기
            if (sayWords.contains(words[i])) {
                int[] tmp = {personNumber, turnCount};
                return tmp;
            }
            
            sayWords.add(words[i]);
                
            if (personNumber == n) {
                personNumber = 1;
                turnCount ++;
            } else {
                personNumber++;
            }
        }
        
        return answer;
    }
}