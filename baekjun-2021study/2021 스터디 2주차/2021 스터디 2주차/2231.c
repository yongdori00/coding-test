#include<stdio.h>

int main() {
	int num, pow = 0;
	int tempnum1, tempnum2, answer = 0;
	int tempanswer;

	scanf("%d", &num);
	tempnum1 = num;
	while (tempnum1) {
		tempnum1 /= 10;
		pow++;
	}

	tempnum1 = num - pow * 9;

	while (tempnum1 < num) {
		tempnum2 = tempnum1;
		tempanswer = tempnum2;
		while (tempnum2) {
			tempanswer += tempnum2 % 10;
			tempnum2 /= 10;
		}
		if (tempanswer == num) {
			answer = tempnum1;
			break;
		}
		tempnum1++;
		answer = 0;
	}
	printf("%d", answer);

}