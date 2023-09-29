class Solution {
    public int solution(int num) {
        int answer = 0;
        
        long tmp = (long)num;
        
        while (tmp != 1) {
            answer ++;
            
            if (tmp % 2 == 0) {
                // 짝수일 때
                tmp = tmp / 2;
            } else {
                // 홀수일 때
                tmp = tmp * 3 + 1;
            }
                        
            if (answer >= 500) {
                return -1;
            }
            
        }
        
        return answer;
    }
}