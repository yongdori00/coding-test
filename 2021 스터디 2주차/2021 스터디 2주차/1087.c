#include<stdio.h>

int main() {
	int F, answer = 1;

	scanf("%d", &F);

	for (int i = 1; i <= F; i++) {
		answer *= i;
	}

	printf("%d", answer);
}