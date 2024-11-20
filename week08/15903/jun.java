import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer token;

        token = new StringTokenizer(input.readLine());

        int number_cards = Integer.parseInt(token.nextToken());
        long add_times = Long.parseLong(token.nextToken());
        

        // 2 3 6
        // 5 5 6    :1 
        // 16

        // 1 2 3 4
        // 3 3 3 4 : 1
        // 6 6 3 4 : 2
        // 19
        PriorityQueue<Long> cards = new PriorityQueue<>();
        token = new StringTokenizer(input.readLine());

        for(int i =0; i< number_cards; i++) {
            long num = Long.parseLong(token.nextToken());
            cards.offer(num);
        }

        

        for(long i = 0; i < add_times; i++) {
            long num1 = cards.poll();
            long num2 = cards.poll();
   
            long total = num1+ num2;
            
            cards.offer(total);
            cards.offer(total);
        }

        long anwser = 0;

        for(int i =0; i< number_cards; i++) {
            long number = cards.poll();
            anwser += number;
        }
        
        output.write(String.valueOf(anwser));

        input.close();
        output.close();
    }
}
