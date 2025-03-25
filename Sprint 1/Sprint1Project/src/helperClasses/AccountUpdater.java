package helperClasses;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

// handles adding, removing and updating records in the text files
// In the next sprint, most of these methods will do the same things, but in a database
public class AccountUpdater {
    // appends a record to the end of the text file entered
    public static void appendRecord(String dataToAppend, String fileName) {
        try (PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(fileName, true)))) {
            out.println(dataToAppend);
        } catch (IOException e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }

    // finds the account by searching for the name
    public static String findAccountbyName(String name, String filename) {
        String record = "";
        try {
            File myObj = new File(filename);
            Scanner fileReader = new Scanner(myObj);
            while (fileReader.hasNextLine()) {
                record = fileReader.nextLine();
                if (record.split("\\|", 3)[1].equals(name)) {
                    fileReader.close();
                    return record;
                }
            }
            fileReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
          e.printStackTrace();
        }
        return "";
    }

}
