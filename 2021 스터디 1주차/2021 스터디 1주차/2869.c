#include<stdio.h>

int main() {
	int A, B, V;
	int day;

	scanf("%d %d %d", &A, &B, &V);

	V -= A;
	day = V / (A - B);
	if (V > day * (A - B))
		day++;

	printf("%d", day + 1);
}