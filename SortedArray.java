package Recursion;

import org.jetbrains.annotations.Contract;
import org.jetbrains.annotations.NotNull;

public class SortedArray {
    public static void main(String[] args) {
        int[] check = {1,2,3,4,5,6,7,8};
        //System.out.println(sorted(check));
        System.out.println(recursionsort(check, 0, 1));
    }

    @Contract(pure = true)
    static boolean sorted(int @NotNull [] arr) {
        for (int i = 0; i <= arr.length; i++) {
            if(arr[i] > arr[i+1]) {
                return false;
            }
        }
        return true;
    }

    static boolean recursionsort(int[] arr, int pointer, int subsequent) {
        if (subsequent >= arr.length) {
            return true;
        }
        if (arr[pointer] > arr[subsequent]) {
            return false;
        }
        return recursionsort(arr, pointer+1, subsequent+1);
    }

}
