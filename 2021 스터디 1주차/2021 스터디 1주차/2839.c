#include<stdio.h>

int main() {
	int N, num;
	int result = -1;

	scanf("%d", &N);

	num = N / 5;

	while (num >= 0) {
		int number = N - num * 5;
		if (!(number % 3)) {
			result = number / 3 + num;
			break;
		}
		num--;
	}
	printf("%d", result);
}