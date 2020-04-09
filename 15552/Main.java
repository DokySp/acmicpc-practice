import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;


// 자바로 하는 경우, 클래스 이름을 Main으로 설정해야 백준에서 오류가 안남!
public class Main{
	
    public static void main(String args[]){
		
        // Scanner scan = new Scanner(System.in);
		// Scanner는 버퍼를 사용하지 않아 속도가 느리다! (버퍼 -> 캐시 개념!)
		// https://coding-factory.tistory.com/251 (코드설명)
		// https://jhnyang.tistory.com/92 (그림설명)
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		
		try {
			int ts = getNum(br);
			
			for(int T=0; T<ts; T++)
				sb.append(getNum(br)+getNum(br)+"\n");
				// String[] a = br.readLine().split(" ");
				// sb.append(Integer.parseInt(a[0])+Integer.parseInt(a[1])+"\n");
				// split(), parseInt()가 느린 것으로 추정
			
			bw.write(sb.toString());
			bw.flush(); // 남아있는 정보를 모두 출력
			bw.close(); // 이 두개를 반드시 해주어야 한단다..
			
		} catch(IOException e){}

        return;
    }
	
	// https://www.acmicpc.net/source/17026556 참고
	public static int getNum(BufferedReader br) throws IOException {
		
		int tmp = br.read();
		int num = 0;
		
		while('0'<= tmp && tmp <= '9'){
			num = num*10 + (tmp-'0');
			tmp = br.read();
		}
		
		return num;
	}

}