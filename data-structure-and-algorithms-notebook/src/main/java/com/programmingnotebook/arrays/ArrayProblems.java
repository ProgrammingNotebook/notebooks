package com.programmingnotebook.arrays;

import java.util.Arrays;

public class ArrayProblems {

    public int minimumDistanceProblem(int[] arrayA, int[] arrayB) {

        if (arrayA == null || arrayB == null) return 0;
        int length = arrayA.length;
        if (length < 1 || arrayB.length != length) return 0;

        int minimum = Math.abs(arrayA[0] - arrayB[0]);
        if (length == 1) return minimum;

        for (int i = 1; i < length; i++)
            if (Math.abs(arrayA[i] - arrayB[i]) < minimum)
                minimum = Math.abs(arrayA[i] - arrayB[i]);

        return minimum;
    }

    @SuppressWarnings("unused")
    // Given an array of integers, how would you find the largest element in the array?
    public int findLargest(int[] array) {

        int largest = array[0];

        if (array.length < 100) {
            for (int e : array)
                if (e > largest) largest = e;
        } else {
            int[] sortedArray = sort(array);
            return sortedArray[sortedArray.length - 1];
        }
        return largest;

    }

    private int[] sort(int[] array) {
        Arrays.sort(array);
        return array;
    }
}
