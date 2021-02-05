#include<stdio.h>

int main() {
	int num, tempsmall, tempbig, even, isPrime;

	scanf("%d", &num);

	while (num > 0) {
		scanf("%d", &even);
		int i = even / 2;

		while (i >= 0) {
			isPrime = 1;
			for (int k = 2; k * k <= i; k++) {
				if (i % k == 0) {
					isPrime = 0;
					break;
				}
			}
			if (isPrime == 1) {
				for (int k = 2; k * k <= even - i; k++) {
					if ((even - i) % k == 0) {
						isPrime = 0;
						break;
					}
				}
			}
			if (isPrime == 1) {
				tempsmall = even - i;
				tempbig = i;
				break;
			}
			i++;
		}
		printf("%d %d\n", tempsmall, tempbig);
		num--;
	}
}