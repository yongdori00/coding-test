#include<stdio.h>
#include<string.h>

int main() {
	char A[10001] = { 0 }, B[10001] = { 0 }, result[10001] = { 0 };
	int lenA, lenB, longlen, shortlen, templenA, templenB;
	int i = 0;
	char lifting, temp;

	scanf("%s %s", A, B);

	lenA = strlen(A);
	lenB = strlen(B);

	longlen = (lenA >= lenB) ? lenA : lenB;

	while (i < lenA) {
		A[i] -= '0';
		i++;
	}

	i = 0;

	while (i < lenB) {
		B[i] -= '0';
		i++;
	}

	i = longlen;
	lifting = 0;
	templenA = lenA;
	templenB = lenB;


	while (i >= 0) {
		if (templenA - 1 >= 0 && templenB - 1 >= 0) {
			temp = A[templenA - 1] + B[templenB - 1] + lifting;
			result[i] = temp % 10;
			lifting = temp / 10;
		}
		else if ((templenA - 1 < 0) && (templenB - 1 < 0)) {
			result[i] = lifting;
		}
		else if (templenA - 1 < 0) {
			temp = (B[templenB - 1] + lifting);
			result[i] = temp % 10;
			lifting = temp / 10;
		}
		else if (templenB - 1 < 0) {
			temp = (A[templenA - 1] + lifting);
			result[i] = temp % 10;
			lifting = temp / 10;
		}
		i--;
		templenA--;
		templenB--;
		temp = 0;

	}

	i = 0;

	while (result[i] == 0)
		i++;

	while (i < longlen + 1) {
		printf("%d", result[i]);
		i++;
	}
}