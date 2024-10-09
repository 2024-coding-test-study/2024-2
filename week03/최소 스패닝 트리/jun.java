import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;


class jun {
    /** LinkedArray 추가하는 함수 */
    public static void add_graph(int x, int y, ArrayList<ArrayList<Integer>> graph, int weight) {
        graph.get(x).add(y);
        graph.get(x).add(weight);
        graph.get(y).add(x);
        graph.get(y).add(weight);
    }

    /** 각각의 idx 탐색 함수 */
    public static long sum_of_graph(int start, ArrayList<ArrayList<Integer>> graph) {
        long value = 0;

        for(int i = 0; i< graph.get(start).size(); i+= 2) {
            int des = graph.get(start).get(i);
            int weight = graph.get(start).get(i+1);
            value += weight;
        }

        return value;
    }


    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer token = new StringTokenizer(input.readLine());
        int vertax = Integer.parseInt(token.nextToken()); // vertax
        int edge = Integer.parseInt(token.nextToken()); // edge

        /** Linked Array 추가 */
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        
        /** 각 정점에 대한 ArrayList 초기화 */
        for(int i = 0; i<= vertax; i++) {
            graph.add(new ArrayList<>());
        }

        /** 깊이 우선 탐색으로 graph가 0이라면 더해주고 방문처리 */

        for(int i =1 ; i<= edge; i++) { // index = graph
            StringTokenizer token2 = new StringTokenizer(input.readLine());

            int x = Integer.parseInt(token2.nextToken());
            int y = Integer.parseInt(token2.nextToken());
            int weight = Integer.parseInt(token2.nextToken());
            
            add_graph(x, y, graph, weight); // 그래프 추가
        }

        long[] result = new long[vertax+1];
        long compare = 2147483647;
                       

        for(int i =1; i<= vertax; i++) {
            result[i] = sum_of_graph(i, graph);
            if (result[i] <= compare) {
                compare = result[i];
            }
        }
        output.write(String.valueOf(compare));

        input.close();
        output.close();
    }
}

