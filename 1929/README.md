# <img src='https://doky.space/assets/icpclev/s2.svg' height=23px> [[1929] 소수 구하기](http://icpc.me/1929)

- **C: [:o:]**
  - 200419
  - 33:00 .42
  - 시도: 2번

### 메모
 - 소수: 1과 자기 자신 이외의 나누어 떨어지는 수가 없는 수.
    - 즉, M이 소수인지 판별하기 위해서는 1~M까지 나누어보고 나머지가 0인 경우가 없는 수를 골라내면 된다! (code2)
    - 문제는.. 이 방법은 시간이 엄청나게 오래걸린다는 것!
       - ```
         M부터 N사이의 모든 수에 대해
          ➡️ 1~(M-1) 부터 1~(N-1)까지의 나눗셈 연산을 해야 한다!
         ```
    - **에라토스테네스의 채**
       - 2, 3을 기준으로 나누어 떨어지는 수를 제거해나가는 방법으로
       - 연산량을 줄여주는 방법!
       - ```
         1부터 1,000,000 사이 소수를 전부 계산한다!
          ➡️ 2의 배수 삭제, 3의 배수 삭제, ...
             뒤로 갈 수록 고려할 경우의 수가 줄어든다!
         ```

### 참고
 - 1은 소수가 아님!
 - [[Wiki]Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithm_complexity)
 - [[Algorithm] 에라토스테네스의 체](https://velog.io/@max9106/Algorithm-%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98-%EC%B2%B4)
 - [에라토스테네스의 체 시간복잡도 #1](http://doocong.com/algorithm/sieve-of-eratosthenes/)
 - [에라토스테네스의 체 시간복잡도 #2](http://blog.naver.com/PostView.nhn?blogId=kks227&logNo=220793360258&redirect=Dlog&widgetTypeCall=true)
