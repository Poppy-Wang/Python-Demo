package lesson4;

import java.util.ArrayList;

public class ArrayListDemo {
	public static void main(String[] args) {
		//ArrayList<String> list=new ArrayList<String>();//只能声明引用类型 int-integer（包装类型）
		ArrayList<Student> list=new ArrayList<Student>();
//		System.out.println(list.size());//获取集合的大小
//		list.add("张三");
//		list.add("李四");
//		list.add("王五");
//		System.out.println(list.size());//alt+向下箭头上下移动该行
//		System.out.println(list.get(0));//获取list集合里面的数据，下标从0开始
//		String removeString=list.remove(0);//移除list集合里的元素
//		System.out.println(removeString);
//		System.out.println(list.size());
//		System.out.println(list.get(0));
//		System.out.println(list.isEmpty());//判断是否是空集合
//		list.add("王五");
//		System.out.println(list);
		//list保存数据:有序可重复
		Student student=new Student();
		list.add(student);
	}
}
