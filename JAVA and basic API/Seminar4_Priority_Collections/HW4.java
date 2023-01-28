package Seminar4_Priority_Collections;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;

public class HW4 {
  
    public static void main(String[] args) {
        ArrayList<String> family = new ArrayList<>();
        ArrayList<String> name = new ArrayList<>();
        ArrayList<String> surname = new ArrayList<>();
        ArrayList<Integer> age = new ArrayList<>();
        ArrayList<Boolean> gender = new ArrayList<>();
        LinkedList<Integer> index = new LinkedList<>();
        // String text = "";
        // try {
        //    FileWriter fileWriter = new FileWriter("db.sql",true);
        //    fileWriter.append("Hello word!"); 
        //    fileWriter.flush();
        //    fileWriter.close(); 

        //     try (FileReader fileReader = new FileReader("db.sql")) {
        //         while (fileReader.ready()) {
        //             text += (char) fileReader.read(); 
        //         }
        //     }
        // } catch (IOException e) {
        //     throw new RuntimeException(e);
        // }

        // String[] str = text.split("\n");
        // System.out.println(str); 

        String text = "";
        try {
            FileWriter fileWriter = new FileWriter("db.sql");
             
            fileWriter.append("Иванов Иван Иванович 36 М\n");
            fileWriter.append("Петрова Татьяна Олеговна 27 Ж\n");
            fileWriter.append("Сидорова Наталья Сергеевна 51 Ж\n");  
            fileWriter.append("Кузнецов Илья Андреевич 25 М\n");
            fileWriter.append("Берёзова Татьяна Викторовна 22 Ж\n");
            fileWriter.append("Гончаров Глеб Николаевич 41 М\n");
            fileWriter.append("Дубровина Мария Игоревна 43 Ж\n"); 
            
            fileWriter.flush();
            fileWriter.close();        
             
            FileReader fileReader = new FileReader("db.sql");
            while ((fileReader.ready())) {
                text += (char) fileReader.read();
             
            }
            
            fileReader.close();

            System.out.println("\nСписок пользоваелей:");
            System.out.println(text);            

        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        String[] str= text.split("\n"); 
                      
        System.out.println("Преобразованный список:");
        for (int i = 0; i < str.length; i++) {
                        String [] strTmp = str[i].split(" ");
                        System.out.printf("%s %s.%s. %s %s\n", strTmp[0], strTmp[1].toUpperCase().charAt(0), strTmp[2].toUpperCase().charAt(0), strTmp[3], strTmp[4]);
                        family.add(strTmp[0]);
                        name.add(strTmp[1]);
                        surname.add(strTmp[2]);
                        age.add(Integer.parseInt(strTmp[3]));
                        gender.add(strTmp[4].equals("М")? false : true);
                        index.add(i);
                    }

        System.out.println("\nСписок отсортированный по возрасту:");

        
        sortListByIndex(age, index);
        printLists(family, name, surname, age, gender, index);
    }

    private static void printLists(ArrayList<String> list1, ArrayList<String> list2, ArrayList<String> list3,
                                       ArrayList<Integer> list4, ArrayList<Boolean> list5, LinkedList<Integer> indexes) {

        for (Integer i : indexes) {
            String gender = (list5.get(i).equals(true) ? "Ж" : "М");
            System.out.printf("%s %s.%s. %s %s\n", list1.get(i), list2.get(i).toUpperCase().charAt(0),
                    list3.get(i).toUpperCase().charAt(0), list4.get(i), gender);
        }
    }

    private static void sortListByIndex(ArrayList<Integer> arrayToSort, LinkedList<Integer> ind) {
        ArrayList<Integer> arr = new ArrayList<>(arrayToSort);

        for (int i = 0; i < arr.size(); i++) {
            for (int j = 0; j < arr.size() - 1; j++) {
                if (arr.get(j) > arr.get(j + 1)) {
                    int tmp = ind.get(j);
                    ind.set(j, ind.get(j + 1));
                    ind.set(j + 1, tmp);

                    tmp = arr.get(j);
                    arr.set(j, arr.get(j + 1));
                    arr.set(j + 1, tmp);
                }
            }
        }
    }
}
