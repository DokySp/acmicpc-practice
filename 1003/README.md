# [[1003] 피보나치 함수](http://icpc.me/1003)

- node.js: [:o:]
  - 200405
  - 54:42 .52 
  - 시도: 2번


### 메모
 - 재귀함수와 반복함수
   - 재귀함수는 구조상 시간이 오래 걸리는 구조이다.
   - 재귀함수가 계산이 오래 걸리는 이유 -> complete binary tree 구조로 계산됨 -> 시간복잡도: O(2^n)
   - ![트리구조](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F216DF84957B87E6125)
   - 따라서, 문제 조건인 0.25초 이내에 풀어내기 위해서는 재귀함수로 짜여진 피보나치 함수를 반복함수로 바꾸어주어야 한다!
   - 규칙성을 찾아내는데 시간이 많이 걸렸다..

### 참고
 - [피보나치 수열 알고리즘을 해결하는 5가지 방법](https://shoark7.github.io/programming/algorithm/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%84-%ED%95%B4%EA%B2%B0%ED%95%98%EB%8A%94-5%EA%B0%80%EC%A7%80-%EB%B0%A9%EB%B2%95)
 - [Binary Tree](https://greatzzo.tistory.com/14)
 - [빅오 표기법(Big-O notation), 시간복잡도, 공간복잡도](https://blog.naver.com/kks227/220769859177)
