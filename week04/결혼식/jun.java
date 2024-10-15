import java.beans.DefaultPersistenceDelegate;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.text.BreakIterator;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main {
    public static void add_graph(int x, int y, int[][] graph) {
        graph[x][y] = 1;
        graph[y][x] = 1;
    }

    public static int BFS(int start, int graph[][], boolean check[]) {
        int dept = 0;
        int count = 0;
        
        Queue<Integer> q = new LinkedList<Integer>();
        
        q.offer(start);        
        check[start] = true;

        while(!q.isEmpty()) {
            int _size = q.size();

            for(int i =0; i< _size; i++) {
                int nodeIndex = q.poll();

                for(int j = 1; j < graph[nodeIndex].length; j++) {
                    if(!check[j] && graph[nodeIndex][j] == 1) {
                        check[j] = true;
                        q.offer(j);

                        if(dept == 0 || dept == 1) {
                            count++;
                        }
                    }
                }
            }
            dept++;
            if(dept == 2){
                break;
            }
        }
        return count;
    }   

    public static void main(String[] args) throws  IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        int vertax = Integer.parseInt(input.readLine());
        int repeat_num = Integer.parseInt(input.readLine());
        int graph[][] = new int[vertax+1][vertax+1];
        boolean check[] = new boolean[vertax+1];

        for(int i =1; i<= repeat_num; i++) {    
            StringTokenizer token = new StringTokenizer(input.readLine());

            int x = Integer.parseInt(token.nextToken());
            int y = Integer.parseInt(token.nextToken());

            add_graph(x, y, graph);
        }

        output.write(String.valueOf(BFS(1, graph, check)));

        input.close();
        output.close();
    }
} 
