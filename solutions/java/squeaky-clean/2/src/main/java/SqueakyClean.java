class SqueakyClean {
    static String clean(String identifier) {
        String identifier2 = identifier.replace(" ", "_");
        identifier2 = identifier2.replace("4", "a").replace("3", "e").replace("0", "o").replace("1", "l").replace("7", "t");

        StringBuilder sb = new StringBuilder(identifier2.length());
        
        boolean replaceNext = false;
        for (int i = 0; i<identifier2.length(); i++) {
            char c = identifier2.charAt(i);

            if (replaceNext) {
                sb.append(Character.toUpperCase(c));
                replaceNext = false;
            } else if (c == '-') {
                replaceNext = true;
            } else if (c == '_') {
                sb.append(c);
            } else if (!Character.isLetter(c)) {
                ;
            } else if (replaceNext == true) {
                ;
            } else {
                sb.append(c);
                replaceNext = false;
            }
        }

        String identifier3 = sb.toString();
        return identifier3;
    }
}
