import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        int repeat_num = Integer.parseInt(input.readLine());

        long[] sour = new long[repeat_num];
        long[] bitter = new long[repeat_num];


        for(int i =0; i< repeat_num; i++) {
            StringTokenizer token = new StringTokenizer(input.readLine());

            sour[i] = Long.parseLong(token.nextToken());
            bitter[i] = Long.parseLong(token.nextToken());
        }
        /**
              0001    0111
              0010    0110
              0011    1000
              0100    1001
         */
         /**
              11000  10111
                24      23
          */

          // 브루트포스..?

        int bit_king =  1<<repeat_num; // 재료들의 경우의 수 2^repeat_num
        int ans = Integer.MAX_VALUE;

        for(int i =1; i< bit_king; i++) { // 모든 경우의 수 조합이 1부터 시작
            int times_sour = 1;             // 몇 가지의 종류의 재료를 선택하였을 때
            int add_bitter = 0;

            /**
             *  i=0 0000    i=4 0100
             *  i=1 0001    i=5 0101
             *  i=2 0010      .
             *  i=3 0011      .
             */

            
            for(int j = 0; j< repeat_num; j++) { // 모든 경우의 수
                if((i & (1 << j)) > 0) {        
                    /** 
                     * i는 조합의 모든 경우의 수를 count시키고
                     * j는 조합을 bit연산시켜서 해당하는 경우의 수를 찾아낸다.
                     * 
                     * i와j를 AND연산을 시켜서 해당하는 경우의 수를 찾아낸다.
                     */
                    times_sour *= sour[j];
                    add_bitter += bitter[j];
                }
            }
            int com = Math.abs(times_sour - add_bitter);

            if(com < ans) {
                ans = com;
            }
        }
        output.write(String.valueOf(ans)+"\n");

        input.close();
        output.close();
    }
}
