import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

class Student implements Comparable<Student>{
    int age;
    String name;
    Student(int age, String name) {
        this.age = age;
        this.name = name;
    }
    public int compareTo(Student o) {
        return 1;
    }
}

public class ComparatorVSComparable {

    public static Comparator<Student> l1 = new Comparator<Student>() {
        public int compare(Student o1, Student o2){
            return 1;
        }
    };
    
    public static void main(String[] args) {
        System.out.println("->>--->");
        List<Student> students = new ArrayList<>();
        students.sort(l1);
    }
}
