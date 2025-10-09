import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class LogLevels {
    
    public static String message(String logLine) {
        String s = logLine.split(":")[1];
        return s.trim();
    }

    public static String logLevel(String logLine) {
        Pattern pattern = Pattern.compile("[A-Z]+");
        Matcher matcher = pattern.matcher(logLine);
        matcher.find();
        return matcher.group().toLowerCase();
    }

    public static String reformat(String logLine) {
        Pattern pattern = Pattern.compile("[A-Z]+");
        Matcher matcher = pattern.matcher(logLine);
        matcher.find();
        String logLevel = matcher.group().toLowerCase();
        return message(logLine) + " (" + logLevel + ")";
    }
}
