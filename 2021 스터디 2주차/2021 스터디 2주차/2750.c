#include<stdio.h>
#include<stdlib.h>

int compare(const void* a, const void* b)
{
    int num1 = *(int*)a;
    int num2 = *(int*)b;

    if (num1 < num2)
        return -1;

    if (num1 > num2)
        return 1;

    return 0;
}

int main() {
    int num, * arr, i = 0;

    scanf("%d", &num);

    arr = (int*)calloc(num, sizeof(int));

    for (i = 0; i < num; i++)
        scanf("%d", &arr[i]);

    qsort(arr, num, sizeof(int), compare);

    for (i = 0; i < num; i++)
        printf("%d\n", arr[i]);
}