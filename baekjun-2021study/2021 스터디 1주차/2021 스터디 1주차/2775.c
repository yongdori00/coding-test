#include<stdio.h>
#include<stdlib.h>

int main() {
	int T, k, n, sum = 0;
	int* floorlow, *floorhigh;

	scanf("%d", &T);
	
	while (T > 0) {
		scanf("%d %d", &k, &n);

		floorlow = calloc(n + 1, sizeof(int));
		floorhigh = calloc(n + 1, sizeof(int));

		for (int i = 1; i <= n; i++)
			floorlow[i] = i;

		for (int i = 0; i < k; i++) {
			for (int j = 1; j <= n; j++) {
				for (int l = 1; l <= j; l++) {
					floorhigh[j] += floorlow[l];
				}
			}
			for (int j = 1; j <= n; j++) {
				floorlow[j] = floorhigh[j];
				floorhigh[j] = 0;
			}
		}
		printf("%d\n", floorlow[n]);

		T--;
		free(floorlow);
		free(floorhigh);
	}
}