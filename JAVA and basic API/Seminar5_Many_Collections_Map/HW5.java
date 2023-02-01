import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Set;

public class HW5 {
    public static void main(String[] args) throws Exception {
// 1. Создать словарь HashMap. Обобщение <Integer, String>.
// 2. Заполнить пятью ключами (индекс, ФИО+Возраст+Пол "Иванов Иван Иванович 28 м"), добавить ключ, если не было!)
        Map<Integer, String> hashMap = new HashMap<>();
        hashMap.put(0, "Иванов Иван Иванович 28 м");
        hashMap.put(1, "Чудная Елена Игоревна 36 ж");
        hashMap.put(2, "Дубровина Мария Сергеевна 43 ж");
        hashMap.put(3, "Кузнецов Илья Андреевич 25 м");
        hashMap.put(4, "Берёзова Татьяна Викторовна 37 ж");
            
        for (Map.Entry<Integer, String> iterable_element : hashMap.entrySet()) {
            System.out.println("ключ: "+iterable_element.getKey()+"; "+"значение: "+ iterable_element.getValue());
        } 
    
        ArrayList<Integer> age = new ArrayList<>();
        ArrayList<String> family = new ArrayList<>();
        ArrayList<String> name = new ArrayList<>();
        ArrayList<String> soname = new ArrayList<>();
        LinkedList<Integer> index = new LinkedList<>();
    
    // 3. Изменить значения сделав пол большой буквой.
        System.out.println("\nВывод, где категория 'пол' с большой буквы: ");
        Set<Integer> keySet = hashMap.keySet();
        for (int i = 0; i < keySet.size(); i++) {
            String [] string = (hashMap.get(keySet.toArray()[i]).split("\n"));   
            for (int j = 0; j < string.length; j++) {
                String [] tmp = string[j].split(" ");
                System.out.println(tmp[0]+ " " + tmp[1] + " "+ tmp[2] +" "+ tmp[3]+" "+tmp[4].toUpperCase());
            } 
        }
    // 4. Пройти по коллекции и вывести значения в формате Фамилия инициалы "Иванов И.И."
    System.out.println("\nВ формате фамилия инициалы: Иванов И.И.");
        for (int i = 0; i < keySet.size(); i++) {
            String [] string = (hashMap.get(keySet.toArray()[i]).split("\n"));   
            for (int j = 0; j < string.length; j++) {
                String [] tmp = string[j].split(" ");
                index.add(i);
                age.add(Integer.valueOf(tmp[3]));
                family.add(tmp[0]+" ");
                name.add(tmp[1].charAt(0) + ".");
                soname.add(tmp[2].charAt(0) + ".");
                System.out.printf(family.get(index.get(i)));
                System.out.printf(name.get(index.get(i)));
                System.out.printf(soname.get(index.get(i)));
                System.out.println();
            } 
        }

    // 5. *Сортировать значения по возрасту и вывести отсортированную коллекцию, как в четвёртом пункте.
        ArrayList<Integer> tmp = new ArrayList<>(age);
        Collections.sort(tmp);
        for (int i = 0; i < tmp.size(); i++) {
            int j = age.indexOf(tmp.get(i));
            index.set(i, j);
        }
    
        System.out.println("\nКоллекция, отсортированная по возрасту: ");
        for (int i = 0; i < index.size(); i++) {
            System.out.printf(family.get(index.get(i)));
            System.out.printf(name.get(index.get(i)));
            System.out.printf(soname.get(index.get(i)));
            System.out.println();
          }
    }
}
