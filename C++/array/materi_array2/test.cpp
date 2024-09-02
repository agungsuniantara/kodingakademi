#include <iostream>
#include <functional>
#include <algorithm>

using namespace std;

void klargest (int nums[], int n, int k)
{
    sort(nums, nums + n, greater<int>());
    cout << "\nLargest " << k << " Elements: ";
    for (int i = 0; i < k; i++)
    {
        cout << nums << " ";
    }
}

int main()
{
    int nums[] = {4, 5, 9, 12, 9, 22, 45, 7};
    int n = sizeof(nums)/sizeof(nums[0]);
    cout << "Original array: ";
    for (int i=0; i < n; i++)
    {
        cout << nums << " ";
    }
    int k = 4;
    klargest(nums, n, k);

    return 0;
}
