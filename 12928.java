class Solution {
    public int solution(int n) {
        int answer = 0;
        
        int yaksu = n;
        while (yaksu > 0) {
            
            if (n % yaksu == 0) {
                answer += yaksu; 
            }
            
            yaksu--;
        }
        
        return answer;
    }
}