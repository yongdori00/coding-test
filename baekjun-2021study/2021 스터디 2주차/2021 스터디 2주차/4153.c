#include<stdio.h>
#include<math.h>

int main() {
	int x, y, z, h, w, hypo;

	scanf("%d %d %d", &x, &y, &z);

	while ((x || y || z) != 0) {
		if (x >= y) {
			h = y;
			if (x >= z) {
				hypo = x;
				w = z;
			}
			else if (z >= x) {
				hypo = z;
				w = x;
			}
		}
		else if (y > x) {
			h = x;
			if (y >= z) {
				hypo = y;
				w = z;
			}
			else if (z >= y) {
				hypo = z;
				w = y;
			}
		}

		if ((int)pow(hypo, 2) == (int)pow(w, 2) + (int)pow(h, 2))
			printf("right\n");
		else
			printf("wrong\n");

		scanf("%d %d %d", &x, &y, &z);
	}
}