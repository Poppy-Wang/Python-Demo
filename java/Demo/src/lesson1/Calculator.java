package lesson1;

import java.util.Scanner;
//������ִ�е�jar����ͨ��bat�����������г���
public class Calculator {
public double add(double a,double b){
	return a+b;
}
public double minus(double a,double b){
	return a-b;
}
public double multiply(double a,double b){
	return a*b;
}
public double divide(double a,double b){
	return a/b;
}
public static void main(String[] args) {
	Scanner scan=new Scanner(System.in);//������,System.inΪϵͳ��������
	Calculator calculator=new Calculator();
	//�����һ������
	System.out.println("�������һ������");
	double a=scan.nextDouble();
	//���������
	System.out.println("�����������");
	String operate=scan.next();
	//����ڶ�������
	System.out.println("������ڶ�������");
	double b=scan.nextDouble();
	//��������������������Ӧ�ķ��������������
	double result=0.0;
	if("+".equals(operate)){//equals�ж������ַ����Ƿ�һ��
		//��ɼӷ�����
		result=calculator.add(a, b);
	}else if ("-".equals(operate)) {
		//��ɼ�������
		result=calculator.minus(a, b);
	}else if ("*".equals(operate)) {
		////��ɳ˷�����
		result=calculator.multiply(a, b);
	}else if("/".equals(operate)){
		////��ɳ�������
		result=calculator.divide(a, b);
	}else{
		System.out.println("��������������");
	}
	//������
	System.out.println("���Ϊ:"+result);
}
}

