#include<stdio.h>
#define _USE_MATH_DEFINES
#include<math.h>

int main() {
	int r;
	float uclid = 0.0, taxi = 0.0;

	scanf("%d", &r);

	printf("%.6f %.6f", r * r * M_PI, 2.0 * r * r);
}