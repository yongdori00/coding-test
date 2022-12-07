#include<stdio.h>

int main() {
	int layer = 1, index = 0;
	int num;

	scanf("%d", &num);

	while (num > 0) {
		num -= layer;
		index++;
		layer = index * 6;
	}
	printf("%d", index);
}