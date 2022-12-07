#include<stdio.h>
#include<stdlib.h>

int main() {
	float tempmean = 0;
	int n, cnt = 0, modeNum = 0, num = 0, sum = 0, median = 0, median_cnt = 0, max = 0, min = 4000, escape = 0, mean = 0;
	int* n_list;
	int n_mode[8001] = { 0 };

	scanf("%d", &n);

	n_list = (int*)calloc(n, sizeof(int));

	for (int i = 0; i < n; i++) {
		scanf("%d", &n_list[i]);
		sum += n_list[i];
		n_mode[n_list[i] + 4000] += 1;
		if (n_list[i] > max)
			max = n_list[i];
		if (n_list[i] < min)
			min = n_list[i];
	}

	for (int i = 0; i < 8001; i++) {
		if (n_mode[i] > num) {
			num = n_mode[i];
			modeNum = i - 4000;
		}
	}

	for (int i = 0; i < 8001; i++) {
		if (n_mode[i] == num) {
			cnt++;
		}
		if (cnt == 2) {
			modeNum = i - 4000;
			break;
		}
	}

	tempmean = sum / (float)n;
	if (tempmean - sum / n >= 0.5)
		mean = sum / n + 1;
	else
		mean = sum / n;

	for (int i = 0; i < 8001; i++) {
		while (n_mode[i] != 0) {
			median_cnt += 1;
			n_mode[i] -= 1;
			if (median_cnt > (n / 2)) {
				median = i - 4000;
				escape = 1;
				break;
			}
		}
		if (escape == 1)
			break;
	}


	printf("%d\n", mean);
	printf("%d\n", median);
	printf("%d\n", modeNum);
	printf("%d\n", max - min);
}