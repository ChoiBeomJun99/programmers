class Solution {
    public int solution(int n) {    
        int answer = 0;
        
        int tmp = 1;
        while (n > tmp) {
            if (n % tmp == 1) {
                return tmp;
            }
            
            tmp ++;
        }
        
        return answer;
    }
}