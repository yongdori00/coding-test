#include<stdio.h>

int main() {
	int num = 0, series = 0, count = 0;

	scanf("%d", &num);

	while (count < num) {
		series++;
		int sixNum = 0;
		int tempseries = series;
		while (tempseries > 0) {

			if (tempseries % 10 == 6)
				sixNum++;
			else
				sixNum = 0;
			tempseries /= 10;

			if (sixNum == 3)
				break;
		}
		if (sixNum == 3)
			count++;
	}
	printf("%d", series);

	return 0;
}