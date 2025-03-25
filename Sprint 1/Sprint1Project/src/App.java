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
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import helperClasses.AccountUpdater;


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
            userID = createAccount(userType, userIn);
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

    private static int createAccount(String userType, Scanner userIn) {
        if (userType.equals("paitent") || userType.equals("Paitent")) {
            return createPaitAcc(userIn);
        }
        return createDocAcc(userIn);
    }

    // gets doctor information from the user and appends the data to the doctor.txt file
    private static int createDocAcc(Scanner userIn) {
        int maxID = getMaxID("doctor.txt");
        int userID = maxID + 1;
        // adds the user's data to the doctor.txt in the following order with | between them:
        // userID|name|password|phone#|email|institutionName

        System.out.print("Enter your name as: (First Name) (Last Name): ");
        String name = validateInput(userIn, "[A-Z][a-z]+ [A-Z][a-z]+", "(First Name) (Last Name)");

        System.out.print("Enter your password (cannot contain | and must be between 8 and 12 characters): ");
        String password = validateInput(userIn, "[^|]{8,12}", "cannot contain | and must be between 8 and 12 characters");

        System.out.print("Enter your phone number with no separation between digits : ");
        String phoneNum = validateInput(userIn, "[0-9]{10}", "no separation between digits");

        System.out.print("Enter your email as username@email.com");
        String email = validateInput(userIn, "[A-z]+@[A-z]+\\.[A-z]+", "username@email.com");

        System.out.print("Enter your institution name: ");
        String instName = userIn.nextLine();

        String newAccountEntry = String.join("|", Integer.toString(userID), name, password, phoneNum, email, instName);
        AccountUpdater.appendRecord(newAccountEntry, "doctor.txt");
        return userID;

    }

    private static int createPaitAcc(Scanner userIn) {
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

    // takes a user input and verifies that it matches the pattern needed, if it doesn't, it prints the feedback to help 
    // the user input the correct data Ex: for a phone number input, pattern = "[0-9]{3}\.[0-9]{3}\.[0-9]{4}", feeback: "XXX.XXX.XXXX"
    private static String validateInput(Scanner userIn, String pattern, String feedback) {
        Pattern compiledPattern = Pattern.compile(pattern);
        String inputData;
        while (true){
            inputData = userIn.nextLine();
            Matcher matcher = compiledPattern.matcher(inputData);
            boolean matchFound = matcher.find();
            if (matchFound) {
                return inputData;
            }
            System.out.print("Incorrect format. please enter again with the format: " + feedback + " : ");
        }
    }

}
