#include<stdio.h>

int main() {
	int layer = 1, son, mom;
	int num = 0;

	scanf("%d", &num);

	while (num > layer) {
		num -= layer;
		layer++;
	}
	if (layer % 2 == 0) {
		mom = layer - num + 1;
		son = num;
	}else {
		son = layer - num + 1;
		mom = num;
	}
	printf("%d/%d", son, mom);
}