class Solution:
    def select(self, arr, i):
        c = i
        for j in range(i, len(arr)):
            if arr[j] < arr[c]:
                c = j
        return c

    def selectionSort(self, arr, n):
        for k in range(n):
            m = self.select(arr, k)
            arr[k], arr[m] = arr[m], arr[k]
        return arr
