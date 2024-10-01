package com.programmingnotebook.arrays;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

class Arrays001MinimumDifferenceProblemTest {

    private final ArrayProblems arrayProblems = new ArrayProblems();

    @ParameterizedTest
    @MethodSource("arrayInput")
    void minimumDifferenceBetweenTwoArraysTestWhenArraysAreEmpty(int expected, int[] arrayA, int[] arrayB) {
        Assertions.assertEquals(expected, arrayProblems.minimumDistanceProblem(arrayA, arrayB));
    }

    private static Stream<Arguments> arrayInput() {
        return Stream.of(
                Arguments.of(0, null, null),
                Arguments.of(0, null, new int[]{2, 3, 4}),
                Arguments.of(0, new int[]{2, 3, 4}, null),
                Arguments.of(0, new int[]{}, new int[]{}),
                Arguments.of(0, new int[]{}, new int[]{2, 3, 4}),
                Arguments.of(0, new int[]{2, 3, 4}, new int[]{}),

                Arguments.of(1, new int[]{2, 4, 9}, new int[]{5, 6, 8}),
                Arguments.of(2, new int[]{10, 16, 9}, new int[]{8, 7, 3}),
                Arguments.of(5, new int[]{45, 35, 20}, new int[]{50, 45, 5}),
                Arguments.of(24, new int[]{11, 78, 6}, new int[]{93, 102, 89}),
                Arguments.of(10, new int[]{23, 43, 53}, new int[]{11, 33, 43}),
                Arguments.of(95, new int[]{0, 2, 5}, new int[]{100, 99, 100})
        );
    }
}
