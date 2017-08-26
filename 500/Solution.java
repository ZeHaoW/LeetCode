class Solution {
    public String[] findWords(String[] words) {
        String[] str = {"QWERTYUIO", "ASDFGHJKL", "ZXCVBNM"};
        Map<Character, Integer> map = new HashMap();
        for(int i = 0; i < str.length; i++){
            char[] ch = str[i].toCharArray();
            for(int j = 0; j < ch.length; j++){
                map.put(ch[j], i);
            }
        }
        List<String> list = new LinkedList();
        for(int i = 0; i < words.length; i++){
            if(words[i].equals("")) continue;
            char[] ch = words[i].toUpperCase().toCharArray();
            int index = map.get(ch[0]);
            for(int j = 0; j < ch.length; j++){
                if(map.get(ch[j]) != index){
                    index = -1;
                    break;
                }
            }
            if(index != -1)
                list.add(words[i]);
        }
        return list.toArray(new String[0]);
    }
}
