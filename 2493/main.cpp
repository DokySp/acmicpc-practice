#include <iostream>
#define MAX_SIZE 100001
// #define MAX_SIZE 500001

using namespace std;

int main()
{

    freopen("input.txt", "r", stdin);

    int N;
    cin >> N;

    int arr[MAX_SIZE] = {0};
    int ans[MAX_SIZE] = {0};

    int list[MAX_SIZE] = {0}; // 숫자가 아니라 인덱스값을 넣어둠
    int listMax = -1;
    int listIdx = 0;

    int max = 0;
    int maxIdx = 0;

    // memset(arr, 0, sizeof(int) * MAX_SIZE);
    // memset(ans, 0, sizeof(int) * MAX_SIZE);

    for (int i = 0; i < N; ++i)
    {
        int tmp;
        cin >> tmp;
        arr[i] = tmp;
    }

    // 초기 설정
    // max는 마지막 값
    // list에는 마지막값만 넣어둠
    max = arr[N - 1];
    maxIdx = N - 1;
    listMax = -1;
    listIdx = 0;
    // memset(list, 0, sizeof(int) * MAX_SIZE);

    for (int i = N - 2; i >= 0; --i)
    {
        int target = arr[i];
        cout << i << endl;

        // case 1.
        // target이 max보다 작고
        // list의 max (0번째 idx)보다 작은 경우
        // -> list 맨 뒤에 push
        if (target < max && target < listMax)
        {
            cout << "case 1" << endl;
            if (listIdx == 0)
                listMax = arr[i];
            list[listIdx] = i;
            listIdx += 1;
        }

        // case 2.
        // target이 max보다 작고
        // list max보다 큰 경우
        // -> list 전부 빼서 현재 idx로 처리
        // -> target을 list에 push
        if (target < max && target > listMax)
        {
            cout << "case 2" << endl;

            for (int k = 0; k < listIdx; ++k)
                ans[list[k]] = i + 1;

            // 리스트 초기화 후 target push
            // memset(list, 0, sizeof(int) * MAX_SIZE);
            listIdx = 1;
            listMax = arr[i];
            list[0] = i;
        }

        // Case 3.
        // target이 max보다 큰 경우
        // -> list 다 빼서 현재 idx로 처리
        // -> target도 현재 idx로 처리

        if (target > max)
        {
            cout << "case 3" << endl;

            for (int k = 0; k < listIdx; ++k)
                ans[list[k]] = i + 1;
            ans[maxIdx] = i + 1;

            // max 정보 변경
            ans[maxIdx] = i + 1;
            maxIdx = i;
            max = arr[i];

            // 리스트 초기화
            // memset(list, 0, sizeof(int) * MAX_SIZE);
            listIdx = 0;
            listMax = -1;
        }
    }

    for (int i = 0; i < N - 1; i++)
        cout << ans[i] << " ";
    cout << ans[N - 1] << endl;
}