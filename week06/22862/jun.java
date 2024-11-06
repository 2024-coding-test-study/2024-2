import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;


// right값이 배열을 초과하는 경우
public class jun {
/*     public static int solve(int[] array, int delect_cnt, int arr_len) {
        // right 기준
        // 홀수는 pass시킴 delect_cnt 감소
        // 짝수도 pass시키지만 delect_cnt 감소 하지 않음
        // 그러면서 짝수인 수들만 갯수를 세고 만약 홀수가 나왔는데 delect_cnt가 0라면 수를 갱신함

        int answer = 0; // 정답을 배열의 최대 치로 받음
        int left = 1;
        int right = 1;
        int cnt = 0;
        int delect = delect_cnt;

        if(arr_len == 0) {
            return 0;
        }

        while(left <= arr_len) {
            while(right <= arr_len) {
                if(array[right]%2 == 0) { // 짝수라면
                    cnt++;
                } else if(array[right]%2 == 1) { // 홀수라면
                    delect--;
                }
                if(delect < 0) {
                    break;
                }

                right++;
            }
            if(answer <= cnt) {
                answer = cnt;
            }

            cnt = 0;
            delect = delect_cnt;
            left++;
            right = left;
        }
        return answer;
    }

    // 시초가 뜨네?
*/
    public static int solve(int[] array, int delect_cnt, int arr_len) {
        int left = 1;
        int right = 1;
        int answer = 0;
        int cnt =0;
        int delect = delect_cnt;


        while(left <= arr_len) {
            if(array[right]%2 == 0) {
                cnt++;
            } else if(array[right]%2 == 1) {
                delect--;
            }
            

            if((delect < 0) || (array[right] >= arr_len)) {
                if(answer <= cnt) {
                    answer = cnt;
                }
                
                cnt = 0;
                left += 1;
                right = left-1;
                delect = delect_cnt;
            }
            right++;
        }
        return answer;
    }   

    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer token = new StringTokenizer(input.readLine());

        int arr_len = Integer.parseInt(token.nextToken());
        int delect_cnt = Integer.parseInt(token.nextToken());

        int[] array = new int[arr_len+1];

        StringTokenizer token2= new StringTokenizer(input.readLine());

        for(int i =1; i<= arr_len; i++) {
            array[i] = Integer.parseInt(token2.nextToken());
        }

        output.write(String.valueOf(solve(array, delect_cnt, arr_len)));
        input.close();
        output.close();
    }
}
