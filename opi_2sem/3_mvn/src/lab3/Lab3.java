package lab3;

import java.io.Console;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class Lab3 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        
        Double r = new Double(0);
        boolean isNumber = false;
        do {
            System.out.print("Enter a number: ");
            String inpString = sc.nextLine();
            try {
                r = new Double(inpString);
                isNumber = true;
            } catch (NumberFormatException ex) {
                System.out.format("Etered string is not a number, try again.%n");
            }
        } while (!isNumber);

        Contorno s = new Contorno(r);
        ArrayList<Punctum> al = new ArrayList<Punctum>();
        initList(al);

        System.out.println("Points not included in the defined area are:");
        for (Punctum p : al) {
            if (!s.includes(p))
                System.out.format("  {%.1f; %.1f}%n", p.x, p.y);
        }

    }

    private static void initList(ArrayList<Punctum> al) {
        al.add(new Punctum(-5, -5));
        al.add(new Punctum(4, 4));
        al.add(new Punctum(-1, -1));
        al.add(new Punctum(2, 1));
        al.add(new Punctum(0, 0));
        al.add(new Punctum(4, -4));
        al.add(new Punctum(-5, 3));
        al.add(new Punctum(2, -1));
    }
}