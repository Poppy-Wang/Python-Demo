package lesson4;

import java.util.ArrayList;

public class ArrayListDemo {
	public static void main(String[] args) {
		//ArrayList<String> list=new ArrayList<String>();//ֻ�������������� int-integer����װ���ͣ�
		ArrayList<Student> list=new ArrayList<Student>();
//		System.out.println(list.size());//��ȡ���ϵĴ�С
//		list.add("����");
//		list.add("����");
//		list.add("����");
//		System.out.println(list.size());//alt+���¼�ͷ�����ƶ�����
//		System.out.println(list.get(0));//��ȡlist������������ݣ��±��0��ʼ
//		String removeString=list.remove(0);//�Ƴ�list�������Ԫ��
//		System.out.println(removeString);
//		System.out.println(list.size());
//		System.out.println(list.get(0));
//		System.out.println(list.isEmpty());//�ж��Ƿ��ǿռ���
//		list.add("����");
//		System.out.println(list);
		//list��������:������ظ�
		Student student=new Student();
		list.add(student);
	}
}
