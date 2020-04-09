#include <stdio.h>
#include <stdlib.h>

int main(){
	
	int a, b, T, ts = 0;
	int *res = NULL;
	
	scanf("%d", &ts);
	res = (int*)malloc(sizeof(int)*ts);
	
	for(T=0; T<ts; T++){
		scanf("%d", &a);
		scanf("%d", &b);
		res[T] = a+b;
	}
	
	for(T=0; T<ts; T++){
		printf("%d\n", res[T]);
	}
	
	free(res);
	
	return 0;
	
	
}