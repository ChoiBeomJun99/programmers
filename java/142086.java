class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        
        for (int i = s.length() - 1; i > 0; i--) { // 맨 앞부터 비교하기
            int count = -1;
            char tmp = s.charAt(i);
            
            for (int j = i - 1; j >= 0; j--) {
                char tmp2 = s.charAt(j);
                
                if (tmp == tmp2) {
                    count = i - j;
                    break;
                }
            }
            
            answer[i] = count;
        }
    
        answer[0] = -1;
        return answer;
    }
}