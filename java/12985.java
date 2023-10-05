class Solution {    
    public int solution(int n, int a, int b) {
        int answer = 0;
        
        // 항상 a가 작다고 가정한다.
        if (b < a) {
            int tmp = b;
            b = a;
            a = tmp;
        }
        
        
        // 반복을 돌린다.
        while (true) {
            answer ++;
            
            if (a % 2 != 0 && b % 2 == 0 && a+1 == b) {
                break;
            }
            
            // 게임 실행
            if (a % 2 == 0) {
                // 짝수라면
                a /= 2;
            } else {
                a = a / 2 + 1;
            }
            
            if (b % 2 == 0) {
                b /= 2;
            } else {
                b = b / 2 + 1;
            }
            
        }
    
        return answer;
    }
}