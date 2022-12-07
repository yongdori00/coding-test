#include<stdio.h>

int main() {
	int x, y, w, h;
	int result;

	scanf("%d %d %d %d", &x, &y, &w, &h);

	if (x > w / 2) {
		if (y > h / 2) {
			result = ((w - x) <= (h - y)) ? w - x : h - y;
		}
		else {
			result = ((w - x) <= y) ? w - x : y;
		}
	}
	else {
		if (y > h / 2) {
			result = (x <= (h - y)) ? x : h - y;
		}
		else {
			result = (x <= y) ? x : y;
		}
	}
	printf("%d", result);
}