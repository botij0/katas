import java.util.List;

public class lc_58_length_last_word {
    public static void main(String[] args) {
        String s = "   fly me   to   the moon  ";
        System.out.println(lc_58_length_last_word.lengthOfLastWord(s));
    }

    public static int lengthOfLastWord(String s) {
        String[] arr = s.strip().split(" ");
        return arr[arr.length-1].length();
    }
}
