#include<stdio.h>

int main() {
	int M, N, prime, sum = 0, small = 0, isPrime, isPrimeExist = 0;

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
		if (isPrime != 0 && prime != 1) {
			sum += prime;
			if (small == 0)
				small = prime;
			isPrimeExist = 1;
		}
		prime++;
	}
	if (isPrimeExist == 1)
		printf("%d\n%d", sum, small);
	else
		printf("-1");
}