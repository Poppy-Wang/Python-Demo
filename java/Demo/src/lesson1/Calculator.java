package lesson1;

import java.util.Scanner;
//到处可执行的jar包，通过bat批处理来运行程序
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
	Scanner scan=new Scanner(System.in);//输入流,System.in为系统的输入流
	Calculator calculator=new Calculator();
	//输入第一个数据
	System.out.println("请输入第一个数据");
	double a=scan.nextDouble();
	//输入运算符
	System.out.println("请输入运算符");
	String operate=scan.next();
	//输入第二个数据
	System.out.println("请输入第二个数据");
	double b=scan.nextDouble();
	//根据输入的运算符调用相应的方法完成数据运算
	double result=0.0;
	if("+".equals(operate)){//equals判断两个字符串是否一致
		//完成加法运算
		result=calculator.add(a, b);
	}else if ("-".equals(operate)) {
		//完成减法运算
		result=calculator.minus(a, b);
	}else if ("*".equals(operate)) {
		////完成乘法运算
		result=calculator.multiply(a, b);
	}else if("/".equals(operate)){
		////完成除法运算
		result=calculator.divide(a, b);
	}else{
		System.out.println("输入的运算符错误");
	}
	//输出结果
	System.out.println("结果为:"+result);
}
}

