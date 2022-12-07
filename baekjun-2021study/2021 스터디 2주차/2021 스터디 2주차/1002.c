#include<stdio.h>
#include<math.h>

int main() {
	int r1, r2, x1, x2, y1, y2;
	int T;

	scanf("%d", &T);

	while (T--) {
		scanf("%d %d %d %d %d %d", &x1, &y1, &r1, & x2, &y2, &r2);

		float d = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));

		if ((x1 == x2) && (y1 == y2) && (r1 == r2))
			printf("-1\n");
		else if (abs(r1 - r2) < d && d < (r1 + r2))
			printf("2\n");
		else if ((r1 + r2) == d || abs(r1 - r2) == d)
			printf("1\n"); 
		else if ((r1 + r2) < d || abs(r1 - r2) > d)
			printf("0\n");

	}
}