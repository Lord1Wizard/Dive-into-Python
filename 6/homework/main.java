public class main {
    static Integer count;
    public static void main(String[] args){
        Integer[][] field = new Integer[8][8];  
        count=0;  
        field  = generateArray(8,8);   
        arrangement(field, 0);
        
    }
// проверяет бьют ли ферзи друг друга
    private static boolean check(Integer[][] array, int r, int c){
// по столбцам
        for (int i = 0; i < r; i++){
            if (array[i][c] == 1){
                return false;
            }
        }
// по диагонали    
        for (int i = r, j = c; i >= 0 && j >= 0; i--, j--){
            if (array[i][j] == 1){
                return false;
            }
        }
    
// по обратной диагонали 
        for (int i = r, j = c; i >= 0 && j < 8; i--, j++){
            if (array[i][j] == 1){
                return false;
            }
        }    
        return true;
    }

    private static void arrangement(Integer[][] array, int r){
        if (r == 8){
            count=count+1;
            System.out.println(count);
            printArray(array);
            return;
        }    
        // помещаем ферзя на каждую клетку в текущем ряду `r`
        // и повторяем для каждого допустимого движения
        for (int i = 0; i < 8; i++){
            // если никакие два ферзя не бьют друг руга
            if (check(array, r, i)){
                // ставим ферзя на текущую клетку
                array[r][i] = 1;    
                // повторяем для следующей строки
                arrangement(array, r + 1);    
                // возвращаемся назад и удаляем ферзя с текущей клетки
                array[r][i] = 0;
            }
        }
    }
    
    public static Integer[][] generateArray(Integer row, Integer collumn){
        Integer[][] array  = new Integer [row][collumn];
        for (int i = 0; i<array[0].length; i++){
            for (int j = 0; j<array[1].length;j++){
                array[i][j] = 0;
            }          
        }
        return array;
    }

    public static void printArray(Integer[][] array){
        for (int i = 0; i<array[0].length; i++){
            for (int j = 0; j<array[1].length;j++){
                System.out.printf ("%d", array[i][j]);
            }
            System.out.printf ("\n");
        }
        System.out.printf ("\n");
    }
}    