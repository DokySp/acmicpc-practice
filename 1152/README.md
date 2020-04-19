# [[1152] 단어의 개수(B2)](http://icpc.me/1152)

- **C: [:o:]**
  - 200419
  - 27:15 .56
  - 시도: 4번

### 메모
 - C언어의 경우, trim 및 strlen 기능을 직접 구현해야 한다
    - ```C
      int strlen(char* str){
          int i=0;
          while(str[i] != '\0'){
              i++;
          }
          return i;
      }
      ```
    - `trim()` : 앞뒤로 ascii 값이 `32`인 요소를 제거
 - 띄어쓰기를 카운팅할 때, 아무 단어가 없는 공백의 경우를 고려!
