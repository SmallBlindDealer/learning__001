


public class Main {
    public static void main(String args[]) {
        String str = "aabbccybbaa";
        String res = findMax(str, 2);
        System.out.println(res);

        String s1 = "TEST";
        String s2 = "TEST";
        String s3 = new String("TEST");
        System.out.println(s1==s2);
        System.out.println(s1==s3);

        String s4 = new String("TEST");
        System.out.println(s3==s4);
    }

    public static String findMax(String str, Integer maxRemove) {

        String res = "";

        for (int i = 0; i<str.length(); i++) {
            for (int maxR=1; maxR<maxRemove; maxR++) {
                String chrrStr = str.substring(0, i) + str.substring(i+maxR, str.length());
                int l = 0;
                int r = chrrStr.length()-1;
                boolean isP = true;
                while (l<=r) {
                    if (chrrStr.charAt(l)!=chrrStr.charAt(r)) {
                        isP= false;
                        break;
                    }
                    l++;
                    r--;
                }
                if (isP && res.length()<chrrStr.length()) {
                    res = chrrStr;
                }
            }

        }
        return res;
    }
}