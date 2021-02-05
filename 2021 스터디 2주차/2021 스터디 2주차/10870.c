#include<stdio.h>

int main() {
	int front = 0, back = 1, n;

	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		int temp = front + back;
		front = back;
		back = temp;
	}

	printf("%d", front);
}