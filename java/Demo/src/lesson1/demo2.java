package lesson1;
//��������ѧϰ
public class demo2 {
	public static void main(String[] args) {
		//����boolean���ͱ���,ֻ��true����false
		boolean aa=true;
		boolean bb=false;
		//����:byte�������Ϊ127
		byte cc=127;
		short dd=3;
		int ee=34;
		long ff=123;
		//�����ͣ�float,double,С��Ĭ�ϻᱻ����Ϊdouble���ͣ����Զ���float������Ҫ�Ӻ�׺f,float����ռ4���ֽڣ�
		//double����ռ8���ֽڣ�������ת����С���ͱ���Ҫǿ��ת�����˹�����Ҫ�ֶ�ǿ��ת��
		float a=3.14f;
		double b=3.4;
		//�ַ���char
		char c='a';
		//�������ͣ�һ���ڴ��ַ��һ��λ����Ϣ�������飬�࣬�ӿڣ�ö��
		String name="zhangzhang";
		int age=23;
		//System.out.print(name+age);
		//���飺����ȷ��������ȷ��������һ�������ʱ�����ָ������Ĵ�С��������������ͣ�һά���飬��ά����
		//����һά�����﷨���������� [] ��������=new ��������[size]��int [] myArray=new int[3]
		//����һ��������֪������Ԫ��:int myArray={1,2,3}
		String [] arr1=new String[5];
		String [] names={"11","22","33"};
		System.out.println(names[2]);
		int [] Array=new int[5];
		Array[0]=10;
		Array[1]=20;
		Array[2]=30;
		Array[3]=40;
		Array[4]=50;
		System.out.println(Array[0]);
		System.out.println(Array[1]);
		System.out.println(Array[2]);
		System.out.println(Array[3]);
		System.out.println(Array[4]);
		//��ά����
		String [][] names1={{"1","2"},{"3","4"}};
		//ȡ����һ�е�һ��
		System.out.println(names1[0][0]);
		
		
		
}
}