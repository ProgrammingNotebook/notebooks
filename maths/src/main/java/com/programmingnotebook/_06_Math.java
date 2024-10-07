package com.programmingnotebook;

import java.util.*;

@SuppressWarnings("java:S101")
public class _06_Math {

    private _06_Math() {
        throw new UnsupportedOperationException("Instantiation of a static class is prohibited");
    }

    public static List<Integer> getFactors(int number) {

        Set<Integer> factors = new HashSet<>();
        if (number > 0) {
            for (int i = 1; i <= number; i++) {
                if (number % i == 0) factors.add(i);
            }
        }
        return factors.stream().sorted().toList();
    }

    public static String isPrimeOrComposite(int number) {

        List<Integer> factors = getFactors(number);
        if (number < 2) return "neither Prime nor Composite";
        if (factors.size() == 2) return "Prime";
        else return "Composite";
    }

    public static String isEvenOrOdd(int number) {

        if (number % 2 == 0) return "Even";
        return "Odd";
    }

    public static List<Integer> getCommonFactors(List<Integer> numbers) {

        Map<Integer, List<Integer>> numberToFactorsMapping = new TreeMap<>();
        for (int number : numbers) {
            numberToFactorsMapping.put(number, _06_Math.getFactors(number));
        }
        Set<Integer> keys = numberToFactorsMapping.keySet();
        List<Integer> commonFactors = new LinkedList<>();
        for (int key : keys) {
            if (commonFactors.isEmpty())
                commonFactors.addAll(numberToFactorsMapping.get(key));
            else {
                List<Integer> tempValues = numberToFactorsMapping.get(key);
                commonFactors.retainAll(tempValues);
            }
        }
        return commonFactors;
    }

    @SuppressWarnings("all")
    public static List<Integer> getCommonMultiples(List<Integer> numbers) {
        List<Integer> commonMultiples = new ArrayList<>();
        return commonMultiples;
    }
}
