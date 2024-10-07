package com.programmingnotebook;

import lombok.extern.slf4j.Slf4j;

import java.util.List;

@Slf4j
@SuppressWarnings("java:S101")
public class _000_Application {

    public static void main(String[] args) {

        int number = 9735934;
        log.info("Factors of {} are {}", number, _06_Math.getFactors(number));
        log.info("{} is a {} number", number, _06_Math.isPrimeOrComposite(number));
        log.info("{} is {} number", number, _06_Math.isEvenOrOdd(number));

        List<Integer> numbers = List.of(75, 60, 210);
        log.info("Common factors of {} are {}", numbers, _06_Math.getCommonFactors(numbers));
    }
}
