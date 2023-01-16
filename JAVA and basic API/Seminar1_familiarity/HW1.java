import java.util.Random;
public class HW1 {
// 1. Выбросить случайное целое число в диапазоне от 0 до 2000 и сохранить в i
    public static int numberRange(int number) {
        int num = new Random().nextInt(2001);
        return num; 
    }

// 2. Посчитать и сохранить в n номер старшего значащего бита выпавшего числа
    public int mostSignificantBit(int i) {
        int bin = Integer.toBinaryString(i).length();
        return bin;
    } 
    
    public static void main(String[] args) {
        int i =  numberRange(2001);
        System.out.println(i);
     
        int n = Integer.toBinaryString(i).length();
        System.out.println(n);

        // 3. Найти все кратные n числа в диапазоне от i до Short.MAX_VALUE сохранить в массив m1
        int count = 0;
        for (int j = i; j < Short.MAX_VALUE; j++) {
            if (j%n != 0) count++;
        }
        int[] m1 = new int[count];
        count = 0;
        for (int j = i; j < Short.MAX_VALUE; j++) {
            if (j%n != 0) m1[count++] = j;
        }
        // System.out.print(Arrays.toString(arr2));

        // 4. Найти все некратные n числа в диапазоне от Short.MIN_VALUE до i и сохранить в массив m2
        count = 0;
        for (int j = Short.MIN_VALUE; j < i; j++) {
            if (j%n == 0) count++;
        }
        int[] m2 = new int[count];
        count = 0;
        for (int j = Short.MIN_VALUE; j < i; j++) {
            if (j%n == 0) m2[count++] = j;            
        }
        // System.out.print(Arrays.toString(arr1));        
    }
}
