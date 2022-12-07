#include<stdio.h>

int main() {
	int M, prime, isPrime, answer = 0;

	scanf("%d", &M);

	while (M != 0) {
		answer = 0;
		prime = M + 1;
		while (prime <= 2 * M) {
			isPrime = 1;
			for (int i = 2; i * i <= prime; i++) {
				int j = 2;
				if (prime % i == 0) {
					isPrime = 0;
					break;
				}
			}
			if (isPrime == 1 && prime != 1)
				answer++;
			prime++;
		}
		printf("%d\n", answer);
		scanf("%d", &M);
	}
}