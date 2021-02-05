#include<stdio.h>
#include<stdlib.h>

int main() {
	int num, **arr, tempAnswer = 0, answernum = 0;

	scanf("%d", &num);

	arr = (int**)calloc(3, sizeof(int*));
	arr[0] = (int*)calloc(num, sizeof(int));
	arr[1] = (int*)calloc(num, sizeof(int));
	arr[2] = (int*)calloc(num, sizeof(int));

	for (int j = 0; j < num; j++)
		scanf("%d %d", &arr[0][j], &arr[1][j]);

	for (int i = 0; i < num; i++) {
		answernum = 1;
		for (int j = 0; j < num; j++) {
			if (i == j)
				continue;
			if (arr[0][i] < arr[0][j] && arr[1][i] < arr[1][j]) {
				answernum++;
			}
		}
		arr[2][i] = answernum;
	}
	for (int i = 0; i < num; i++)
		printf("%d ", arr[2][i]);
}