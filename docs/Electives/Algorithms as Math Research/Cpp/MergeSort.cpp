#include <iostream>
#include <vector>
using namespace std;


void Merge(int array[], int const Left, int const Mid, int const Right) {
    int const SubArrL = Mid - Left + 1;
    int const SubArrR = Right - Mid;

    int* LeftArray = new int[SubArrL];
    int* RightArray = new int[SubArrR];

    for (int i = 0; i < SubArrL; i++) { LeftArray[i] = array[Left + i]; }
    for (int j = 0; j < SubArrR; j++) { RightArray[j] = array[Mid + 1 + j]; }

    int IndexL = 0;
    int IndexR = 0;
    int IndexM = Left;

    while (IndexL < SubArrL && IndexR < SubArrR) {
        if (LeftArray[IndexL] <= RightArray[IndexR]) {
            array[IndexM] = LeftArray[IndexL];
            IndexL++;
        }
        else {
            array[IndexM] = RightArray[IndexR];
            IndexR++;
        }
        IndexM++;
    }

    while (IndexL < SubArrL) {
        array[IndexM] = LeftArray[IndexL];
        IndexL++;
        IndexM++;
    }

    while (IndexR < SubArrR) {
        array[IndexM] = RightArray[IndexR];
        IndexR++;
        IndexM++;
    }

    delete[] LeftArray;
    delete[] RightArray;
}


void MergeSort(int Array[], int const Begin, int const End)
{
    if (Begin >= End)
        return;
 
    int Mid = Begin + (End - Begin) / 2;
    MergeSort(Array, Begin, Mid);
    MergeSort(Array, Mid + 1, End);
    Merge(Array, Begin, Mid, End);
}

int main() {
    std::ios::sync_with_stdio(false); std::cin.tie(0);
    int t, n, x;
    std::cin >> t;

    for (int i = 0; i < t; i++)
    {
        std::cin >> n;
        int arr[n];

        for (int j = 0; j < n; j++)
        {
            std::cin >> x;
            arr[j] = x;
        }

        MergeSort(arr, 0, n - 1);

        for (int i = 0; i < n; i++) 
        {
            std::cout << arr[i] << " ";
        }
        std::cout << "\n";
    }
    
    std::cout << std::endl;

    return 0;
}