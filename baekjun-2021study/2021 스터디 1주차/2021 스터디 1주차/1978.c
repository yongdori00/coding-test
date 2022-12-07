#include<stdio.h>

int main() {
	int num, prime, answer = 0, isPrime = 1;

	scanf("%d", &num);

	while (num > 0) {
		isPrime = 1;
		scanf("%d", &prime);

		for (int i = 2; i * i <= prime; i++) {
			if (prime % i == 0) {
				isPrime = 0;
				break;
			}
		}
		if (isPrime != 0 && prime != 1)
			answer++;
		num--;
	}
	printf("%d", answer);
}