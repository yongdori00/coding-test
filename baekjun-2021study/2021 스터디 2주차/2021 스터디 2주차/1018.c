#include<stdio.h>
#include<stdlib.h>

char white[8][8] = { {"WBWBWBWB"},
					   {"BWBWBWBW"},
					   {"WBWBWBWB"},
					   {"BWBWBWBW"},
					   {"WBWBWBWB"},
					   {"BWBWBWBW"},
					   {"WBWBWBWB"},
					   {"BWBWBWBW"} };

char black[8][8] = { {"BWBWBWBW"},
					   {"WBWBWBWB"},
					   {"BWBWBWBW"},
					   {"WBWBWBWB"},
					   {"BWBWBWBW"},
					   {"WBWBWBWB"},
					   {"BWBWBWBW"},
					   {"WBWBWBWB"} };
int main() {
	int x, y, tempanswer, banswer, wanswer, answer = 32;
	char** arr;

	scanf("%d%d", &y, &x);

	arr = (char**)calloc(y, sizeof(char*));
	for (int i = 0; i < y; i++)
		arr[i] = (char*)calloc(x, sizeof(char));

	for (int i = 0; i < y; i++)
		scanf("%s", arr[i]);

	for (int i = 0; i < y - 7; i++)
		for (int j = 0; j < x - 7; j++) {
			wanswer = 0;
			banswer = 0;
			for (int k = 0; k < 8; k++)
				for (int l = 0; l < 8; l++)
					if (arr[i + k][j + l] != white[k][l])
						wanswer++;
			for (int k = 0; k < 8; k++)
				for (int l = 0; l < 8; l++) 
					if (arr[i + k][j + l] != black[k][l])
						banswer++;
				
			tempanswer = wanswer <= banswer ? wanswer : banswer;
			answer = answer <= tempanswer ? answer : tempanswer;
		}
	printf("%d", answer);
}