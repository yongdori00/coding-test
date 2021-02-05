#include<iostream>

using namespace std;

int main() {
	int cnt;
	int W, H, num;
	int number, floor;
	int result;

	cin >> cnt;

	while (cnt > 0) {
		cin >> H >> W >> num;

		number = num / H;
		floor = num % H;
		
		if (num % H != 0){
			number++;
		}
		else 
			floor += H;

		result = 100 * floor + number;

		cout << result << endl;
		cnt--;
	}
}