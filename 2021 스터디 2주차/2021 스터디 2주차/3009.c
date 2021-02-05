#include<stdio.h>

int main() {
	int x1 = 0, x2 = 0, y1= 0, y2 = 0, x1cnt = 0, x2cnt = 0, y1cnt = 0, y2cnt = 0;
	int tempx, tempy, x, y;

	for (int i = 0; i < 3; i++) {
		scanf("%d %d", &tempx, &tempy);

		if (i == 0) {
			x1 = tempx;
			y1 = tempy;
			x1cnt++;
			y1cnt++;
			continue;
		}

		if (x1 == tempx) {
			x1cnt++;
		}
		else {
			x2 = tempx;
			x2cnt++;
		}

		if (y1 == tempy) {
			y1cnt++;
		}
		else {
			y2 = tempy;
			y2cnt++;
		}
	}

	if (x1cnt == 1)
		x = x1;
	else
		x = x2;
	if (y1cnt == 1)
		y = y1;
	else
		y = y2;

	printf("%d %d", x, y);
}