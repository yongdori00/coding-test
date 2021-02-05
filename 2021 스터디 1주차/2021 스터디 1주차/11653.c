#include<stdio.h>

int main() {
	int num, i = 2;

	scanf("%d", &num);

	while (num > 1) {
		if (num % i != 0) {
			i++;
			continue;
		}
		num /= i;
		printf("%d\n", i);
	}
}