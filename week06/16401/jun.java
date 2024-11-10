
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;


// 1번째 오류 mid = 0일 때 zero division error
// 2번째 오류 cookie의 개수가 person보다 작을 때 mid값이 1인 경우
// 3번째 오류 if(len_cookie.length < person && high == 1) 시 쿠키 배열의 크기가 person보다 작거나 같아지면 틀림

public class Jun {
    public static int binsearch(int len_cookie[] ,int max, int person) {
        int cnt;
        int low=1;
        int high = max;
        int answer = 0;
        
        if(len_cookie.length < person && high == 1) {
            return 0;
        }

        while(high >= low) {
            int mid = (high+low)/2;
            cnt = 0;

            for(int i =0; i < len_cookie.length; i++) {
                cnt += len_cookie[i]/mid; // 각 개수 구함
            }

            if(cnt >= person) { // mid값이 커져야함
                answer = mid;
                low = mid+1;
            } else {            // mid값이 작아져야함
                high = mid-1;
            }
        }
        return answer;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer token = new StringTokenizer(input.readLine());

        int person = Integer.parseInt(token.nextToken());
        int cookie = Integer.parseInt(token.nextToken());

        int len_cookie[] = new int[cookie];
        StringTokenizer token2 = new StringTokenizer(input.readLine());

        for(int i =0; i< cookie; i++) {
            len_cookie[i] = Integer.parseInt(token2.nextToken());
        }
        Arrays.sort(len_cookie);

        
        output.write(String.valueOf(binsearch(len_cookie, len_cookie[cookie-1], person)));
        
        input.close();
        output.close();
    }
}


