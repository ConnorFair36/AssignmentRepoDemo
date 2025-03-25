/* This is the first and simplest version of our project that implements:
 * 1. creating, updating and deleting paitent/doctor accounts
 * 2. doctors adding and deleting paitents from their own lists
 * 3. doctors updating the medications for their paitents
 * 4. doctors generating a report for a specific paitent
 * 
 * This version stores all relevent data into text files for now, these will be replaced
 * by a database in the next sprint
*/

import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        // ensure all txt files exist
        try {
            // contains data for each paitent
            File paitentFile = new File("paitent.txt");
            paitentFile.createNewFile();
            // contains data for each doctor
            File doctorFile = new File("doctor.txt");
            doctorFile.createNewFile();
            // contains a linking of every doctor to all of their paitents
            File docToPaitFile = new File("docToPait.txt");
            docToPaitFile.createNewFile();
        } catch (IOException e){
            e.printStackTrace();
            System.exit(0);
        }
        // determines if the user is a doctor or a paitent
        Scanner userIn = new Scanner(System.in);
        String userType;
        while (true) {
            System.out.print("Enter if you are a paitent or doctor:");
            userType = userIn.nextLine();
            if (userType.equals("paitent") || userType.equals("Paitent") || userType.equals("doctor") || userType.equals("Doctor")) {
                break;
            }
            System.out.println("invalid input please try again");
        }
        // if the user is new, they will create an account, else
        String isNew;
        while (true) {
            System.out.print("Are you creating a new account? (yes or no):");
            isNew = userIn.nextLine();
            if (isNew.equals("yes") || isNew.equals("no")) {
                break;
            }
            System.out.println("invalid input please only input yes or no");
        }
        int userID;
        if (isNew.equals("yes")) {
            userID = createAccount(userType);
        } else {
            // lets the user login, after 3 failed attempts, the user will be kicked out of the program
            userID = loginUser(userType);
        }
        System.out.println(userID);
        // exit the program once the user has finished their operations
        if (userType.equals("paitent") || userType.equals("Paitent")) {
            paitentOpps(userID);
        } else {
            doctorOpps(userID);
        }

        userIn.close();
    }

    private static int createAccount(String userType) {
        if (userType.equals("paitent") || userType.equals("Paitent")) {
            return createPaitAcc();
        }
        return createDocAcc();
    }

    // gets doctor information from the user and appends the data to the doctor.txt file
    private static int createDocAcc() {
        int maxID = getMaxID("doctor.txt");
        int userID = maxID + 1;
        // TODO: ask for the user's name, password, phone#, email and institution name and verify their validity
        // TODO: add the user's data to the doctor.txt in the following order with | between them:
        // userID|name|password|phone#|email|institutionName
        return userID;

    }

    private static int createPaitAcc() {
        int maxID = getMaxID("paitent.txt");
        int userID = maxID + 1;
        // TODO: ask for the user's name, phone#, email, birthday, sex and insurance provider and verify their validity
        // TODO: add the user's data to the doctor.txt in the following order with | between them:
        // userID|name|password|phone#|email|birthday|sex|insuranceProvider
        return userID;
    }

    // finds the current largest ID in a text file
    private static int getMaxID(String pathname) {
        try {
            File thisFile = new File(pathname);
            Scanner myReader = new Scanner(thisFile);
            String data = "";
            while (myReader.hasNextLine()) {
                data = myReader.nextLine();
            }
            myReader.close();
            String[] lastEntry = data.split("\s");
            int maxID = (data.equals("")) ? -1 : Integer.parseInt(lastEntry[0]);
            return maxID;
        } catch (IOException e){
            e.printStackTrace();
            return -2;
        }
    }

    private static int loginUser(String userType) {
        if (userType.equals("paitent") || userType.equals("Paitent")) {
            return loginPaitent();
        }
        return loginDoctor();
    }

    private static int loginPaitent() {
        // TODO: get the user's name and find it in the paitent.txt file
        // TODO: get a password from the user and verify that it is the same as the one in the record
        // TODO: if the user enters the wrong password 3 times, terminate the program
        return -10000;
    }

    private static int loginDoctor() {
        // TODO: get the user's name and find it in the doctor.txt file
        // TODO: get a password from the user and verify that it is the same as the one in the record
        // TODO: if the user enters the wrong password 3 times, terminate the program
        return -10000;
    }

    private static void paitentOpps(int userID) {
        // TODO: This is where the paitent can view their medications and update their account information
        System.out.println("Doing paitent stuff!");
    }

    private static void doctorOpps(int userID) {
        // TODO: This if where the doctor can add and remove paitents on their list,
        // update medications for users of the list and generate a report for any paitent (this last on might not be doable yet)
        System.out.println("Doing doctor stuff!");
    }

}
