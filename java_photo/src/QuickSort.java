

public class QuickSort {

    private static void swap(int[] arr, int x, int y) {
        int temp = arr[x];
        arr[x] = arr[y];
        arr[y] = temp;
    }

    private static void quick_sort_recursive(int[] arr, int start, int end) {
        if (start >= end)
            return;
        int mid = arr[end];
        int left = start, right = end - 1;
        while (left < right) {
            while (arr[left] <= mid && left < right)
                left++;
            while (arr[right] >= mid && left < right)
                right--;
            swap(arr, left, right);
        }
        if (arr[left] >= arr[end])
            swap(arr, left, end);
        else
            left++;
        quick_sort_recursive(arr, start, left - 1);
        quick_sort_recursive(arr, left, end);
    }


    public static void main(String[] args) {
        int a[] = {2, 5, 9, 3, 8, 4, 7, 6};

        quick_sort_recursive(a, 0, a.length - 1);

        for (Integer i : a) {
            System.out.print(i);
        }
    }
}
