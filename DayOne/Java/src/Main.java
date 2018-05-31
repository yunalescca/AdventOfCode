import java.util.LinkedList;
import java.util.List;

public class Main {

    private static String input = "1122";

    public static void main(String[] args) {
        System.out.println("Hello");

        run();
    }

    private static void run() {


        List<Integer> captcha = new LinkedList<>();

        for (int i = 0; i < input.length(); i++){
            captcha.add(Character.getNumericValue(input.charAt(i)));
        }

    }


}
