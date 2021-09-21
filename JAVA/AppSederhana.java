package app.sederhana;
import java.util.Scanner;
public class AppSederhana {
    public static void main(String[] args) {
        // TODO code application logic here
        /*
        String nama, alamat;
        int usia;
        double berat;

        nama = "Oktavian Andi Cahya Nugraha";
        alamat = "Jati Kulon, Kudus, Jateng";
        usia = 18;
        berat = 58.3;

        System.out.println("Nama\t\t: " + nama);
        System.out.println("Alamat\t\t: " + alamat);
        System.out.println("Usia\t\t: " + usia + " tahun");
        System.out.println("Berat badan\t: " + berat + "kg");
       */
        //variabel
        double sisi_A, sisi_B, sisi, panjang, lebar, tinggi, diameter, alas, phi = 3.14;
        //scanner
        Scanner keyboard = new Scanner(System.in);

        //SEGITIGA
        System.out.println("Menghitung Luas Segitiga");
        System.out.print("Panjang alas : ");
        alas = keyboard.nextDouble();
        System.out.print("Tinggi : ");
        tinggi = keyboard.nextDouble();
        double segitiga = (alas*tinggi)/2;
        //Output
        System.out.println("Luas Segitiga : "+segitiga+"cm^2");
        
        //PERSEGI
        System.out.println("\nMenghitung Luas Persegi");
        System.out.print("Panjang sisi : ");
        sisi = keyboard.nextDouble();
        double persegi = sisi*sisi;
        //output
        System.out.println("Luas Persegi : "+persegi+"cm^2");

        //PERSEGI PANJANG
        System.out.println("\nMenghitung Luas Persegi Panjang");
        System.out.print("Panjang : ");
        panjang = keyboard.nextDouble();
        System.out.print("Lebar : ");
        lebar = keyboard.nextDouble();
        double p_panjang = panjang*lebar;
        //output
        System.out.println("Luas Persegi Panjang : "+p_panjang+"cm^2");

        //LINGKARAN
        System.out.println("\nMenghitung Luas Lingkaran");
        System.out.print("Diameter : ");
        diameter = keyboard.nextDouble();
        double r = diameter/2;
        double lingkaran = phi*r*r;
        //output
        System.out.println("Luas Lingkaran : "+lingkaran+"cm^2");
        
        //TRAPESIUM
        System.out.println("\nMenghitung Luas Trapesium ");
        System.out.print("Sisi A(a-b) : ");
        sisi_A = keyboard.nextDouble();
        System.out.print("Sisi B(d-c) : ");
        sisi_B = keyboard.nextDouble();
        System.out.print("Tinggi : ");
        tinggi = keyboard.nextDouble();
        double trapesium = tinggi*(sisi_A + sisi_B)/2;
        //output
        System.out.println("Luas Trapesium : "+trapesium+"cm^2");
    }
}
