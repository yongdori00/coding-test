#include<stdio.h>
#include<stdlib.h>

int main() {
	int num, a[10001] = { 0 }, index, i = 1;

	scanf("%d", &num);

	while (i <= num) {
		scanf("%d", &index);

		a[index]++;
		i++;
	}
	i = 1;
	while (i < 10001) {
		if (a[i] != 0) {
			printf("%d\n", i);
			a[i]--;
			continue;
		}
		i++;
	}
}