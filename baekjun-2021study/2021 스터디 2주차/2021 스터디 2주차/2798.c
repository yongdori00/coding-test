#include<stdio.h>
#include<stdlib.h>

int main() {
	int sum, sumanswer = 0, num, pick1, pick2, pick3;
	int* arr;

	scanf("%d %d", &num, &sum);
	arr = (int*)calloc(num, sizeof(int));

	for (int i = 0; i < num; i++)
		scanf("%d", &arr[i]);

	for (int i = 0; i < num - 2; i++) {
		for (int j = i + 1; j < num - 1; j++) {
			for (int k = j + 1; k < num; k++) {
				int tempanswer = arr[i] + arr[j] + arr[k];
				if (sumanswer < tempanswer && tempanswer <= sum)
					sumanswer = tempanswer;
				if (sumanswer == sum)
					break;
			}if (sumanswer == sum)
				break;
		}if (sumanswer == sum)
			break;
	}

	printf("%d", sumanswer);
}