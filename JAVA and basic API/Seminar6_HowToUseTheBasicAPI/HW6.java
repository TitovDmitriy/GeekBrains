import java.util.HashMap;
import java.util.Iterator;

public class HW6 {
    private static HashMap<Integer, Object> hMap = new HashMap<>();
    private static final Object OBJ = new Object();
    public static void main(String[] args) {
        addToHMap(0);
        addToHMap(7);
        addToHMap(43);
        addToHMap(13); 
        addToHMap(44);
        addToHMap(1);
        addToHMap(9);
        addToHMap(38);
        addToHMap(10);
        addToHMap(50);
        System.out.println(isEmpty());
        
        printConsole();
        System.out.println();
        try {
            System.out.println(printOneEl(20));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
    //метод добавляет элемент в коллекцию
    public static void addToHMap(Integer number){
        hMap.put(number, OBJ);   
    } 

    //метод возвращает true, если коллекция пуста
    private static boolean isEmpty(){
        return hMap.isEmpty();
    }

    // метод выводит всю коллекцию в консоль
    private static void printConsole(){
        Iterator<Integer> iterator = hMap.keySet().iterator();
        while (iterator.hasNext()){
            System.out.print(iterator.next()+" ");
        }
    }

    //метод  выводит один эллемент коллекции в консоль 
    private static int printOneEl(int index){
        return (Integer)hMap.keySet().toArray()[index];
    }      
}