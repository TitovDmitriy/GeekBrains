// Урок 2. Почему вы не можете не использовать API
// 1. Напишите программу, чтобы найти вхождение в строке (содержащей все символы другой строки).
// 2. Напишите программу, чтобы проверить, являются ли две данные строки вращением друг друга (вхождение в обратном порядке).
// 3. *Напишите программу, чтобы перевернуть строку с помощью рекурсии.
// 4. Дано два числа, например 3 и 56, необходимо составить следующие строки: 3 + 56 = 59 3 – 56 = -53 3 * 56 = 168 Используем метод StringBuilder.append().
// 5. Замените символ “=” на слово “равно”. Используйте методы StringBuilder.insert(),StringBuilder.deleteCharAt().
// 6. *Замените символ “=” на слово “равно”. Используйте методы StringBuilder.replace().
// 7. **Сравнить время выполнения пунка 6 со строкой содержащей 10000 символов "=" средствами String и StringBuilder.

package Seminar2_use_API;

public class HW2 {
    public static void main(String[] args) {
        // 1. Напишите программу, чтобы найти вхождение в строке (содержащей все символы другой строки).
        String str1 = "Example text";
        String str2 = "Example text";
        System.out.println(str1.contains(str2));
        System.out.println(reverseString(str1, str2));
        System.out.println(recursionString(str1));
        // 4. Дано два числа, например 3 и 56, необходимо составить следующие строки: 3 + 56 = 59 
        //    3 – 56 = -53 3 * 56 = 168 Используем метод StringBuilder.append().
        int a = 3;
        int b = 56;
        int sum = a + b;
        int sub = a - b;
        int mult = a * b;
        String plus = " + ";
        String minus = " - ";
        String charmult = " * ";
        String equally  = " = ";
        String strSum = new StringBuilder().append(a).append(plus).append(b).append(equally).append(sum).toString();
        String strSub = new StringBuilder().append(a).append(minus).append(b).append(equally).append(sub).toString();
        String strMult = new StringBuilder().append(a).append(charmult).append(b).append(equally).append(mult).toString();
 
        System.out.println(strSum);
        System.out.println(strSub); 
        System.out.println(strMult);
        // 5. Замените символ “=” на слово “равно”. Используйте методы StringBuilder.insert(),
        // StringBuilder.deleteCharAt().
        System.out.println(replaceEqually(strSum));
        System.out.println(replaceEqually(strSub));
        System.out.println(replaceEqually(strMult));
        System.out.println();

        // 6. *Замените символ “=” на слово “равно”. Используйте методы StringBuilder.replace().
        System.out.println(nextReplaceEquelly(strSum));
        System.out.println(nextReplaceEquelly(strSub));
        System.out.println(nextReplaceEquelly(strMult));
        
        // 7. **Сравнить время выполнения пунка 6 со строкой содержащей 10000 символов "=" средствами String и StringBuilder.
        double begin = System.currentTimeMillis();
        char ch = '=';
        for (int i = 0; i < 10000; i++) {
            strSum += ch;
            strSum += Character.getName(i);
            
        }
        System.out.println(System.currentTimeMillis() - begin);
        
        begin = System.currentTimeMillis();
        StringBuilder sb = new StringBuilder(strSum).append(ch);
        for (int i = 0; i < 10000; i++) {
            sb.append(Character.getName(i));
        }
        System.out.println(System.currentTimeMillis() - begin);
    }
    // 5.
    public static String replaceEqually(String strSum) {
        StringBuilder operation = new StringBuilder(strSum);
        int symbol = operation.indexOf("=");
        return operation.deleteCharAt(symbol).insert(symbol, "равно").toString();
    }

    // 6.
    public static String nextReplaceEquelly(String strSum) {
        StringBuilder operation = new StringBuilder(strSum);
        int symbol = operation.indexOf("=");
        return operation.replace(symbol, symbol + 1, "равно").toString();
    }

    // 2. Напишите программу, чтобы проверить, являются ли две данные строки вращением друг друга (вхождение в обратном порядке).
    public static boolean reverseString(String str1, String str2) {
        return str1.equals(new StringBuilder(str2).reverse().toString());
    }
    // 3. *Напишите программу, чтобы перевернуть строку с помощью рекурсии.
    public static String recursionString(String str1) {
        if (str1.length() <= 1) {
            return str1;
        }
        return recursionString(str1.substring(1)) + str1.charAt(0);
    }
    
}
