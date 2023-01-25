import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;

// 1. Объявить два списка список ArrayList, в каждый добавить по 20 случайных чисел. 
// Удалить из первого списка элементы отсутствующие во втором списке. Отсортировать 
// первый список методом sort класса Collections.
// 2. *Отсортировать второй список методом sort списка и компаратором по уменьшению.
// 3. **Отсортировать первый список пузырьковой сортировкой самостоятельно, без использования
//  доп методов и классов.


public class HW3 {
    
    public static void main(String[] args) {
        ArrayList<Integer> lst1 = new ArrayList<>();
        Random rnd = new Random();
        int size = 20;
        for (int i = 0; i < size; i++) {
            int value = rnd.nextInt(50);
            lst1.add(value);           
        }

        ArrayList<Integer> lst2 = new ArrayList<>();
        rnd = new Random();
        size = 20;
        for (int i = 0; i < size; i++) {
            int value = rnd.nextInt(50);
            lst2.add(value);           
        }
        System.out.println(lst1);
        System.out.println(lst2);
        
        ArrayList<Integer> templst1 = new ArrayList<>(lst1);
        templst1.removeAll(lst2);   
        System.out.println(templst1);    
        lst1.removeAll(templst1); // Удаляем из первого списка элементы, которые отсутствуют во втором списке.

        Collections.sort(lst1); // Сортируем список по возростанию
        System.out.println(lst1);
        
        Collections.reverse(lst1); // Сортируем по уменьшению
        System.out.println(lst1);       
    }
    
}