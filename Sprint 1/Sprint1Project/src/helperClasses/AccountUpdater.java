package helperClasses;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

// handles adding, removing and updating records in the text files
// In the next sprint, most of these methods will do the same things, but in a database
public class AccountUpdater {
    public static void appendRecord(String dataToAppend, String fileName) {
        try (PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(fileName, true)))) {
            out.println(dataToAppend);
        } catch (IOException e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }

    

}
