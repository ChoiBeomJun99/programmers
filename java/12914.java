// 실패 (조합 공식을 이용하려함.)

import java.util.*;
// 1과 2로 순열구하는 문제.

class Solution {
    public long factorial(int n) {
        int result = 1;
        
        for (int j = 1; j <= n; j++) {
            result *= j;
        }
        return result;
    }
    
    public long solution(int n) {
        long answer = 0;
        
        // 2칸 개 수 세기 (최대로)
        long tmp = n;
               
        int countTwo = 0;
        while (tmp > 1) {
            tmp = tmp / 2;
            countTwo ++;
        }
        
        int countOne = 0;
        
        if (countTwo * 2 == n) {
            countOne = 0;
        } else {
            countOne = 1;
        }
                
        // 2의 개수와, 1의 개수로 순열 개수 구하기.
        while (countOne < n) {
            long parent = factorial(countOne + countTwo);
            long child = factorial(countOne) * factorial(countTwo);
                        
            answer += (parent / child % 1234567);
            countTwo --;
            countOne += 2;
        }
        
        answer ++;
        
        return answer;
    }
}


// 성공
// 피보나치 수열과 같은 원리이다.
class Solution {
    public long solution(int n) {        
        long[] dp = new long[2000];
        dp[0] = 1;
        dp[1] = 2;
        
        for (int i = 2; i < 2000; i++) {
            dp[i] = (dp[i-2] + dp[i-1]) % 1234567;
        }
            
        return dp[n-1];
    }
}