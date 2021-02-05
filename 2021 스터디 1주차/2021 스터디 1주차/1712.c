#include<stdio.h>

int main() {
	int A, B, C;
	int count = 0;

	scanf("%d %d %d", &A, &B, &C);

	if (B >= C) {
		printf("-1");
		return 0;
	}
	count = A / (C - B) + 1;
	printf("%d", count);
}