#include<stdio.h>

int main() {
	int M, N, prime, isPrime;

	scanf("%d %d", &M, &N);

	prime = M;

	while (prime <= N) {
		isPrime = 1;
		for (int i = 2; i * i <= prime; i++) {
			int j = 2;
			if (prime % i == 0) {
				isPrime = 0;
				break;
			}
		}
		prime++;
		if (isPrime == 1 && prime != 1)
			printf("%d\n", prime);
	}
}