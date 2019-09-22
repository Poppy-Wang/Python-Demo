package lesson1;

public class demo3 {
	public static void main(String[] args) {
		//运算符分类：算术运算符，关系运算符，逻辑运算符，赋值运算符，其他运算符
		int a=1;
		int b=2;
		int c=4;
		//算术运算符
//		System.out.println(a+b);
//		System.out.println(a-b);
//		System.out.println(a*b);
//		System.out.println(a/b);
//		System.out.println(a%b);//取余数
//		int aa=a++;
//		int bb=++a;
//		System.out.println(aa);
//		System.out.println(bb);
		//关系运算符：分别为小于、小于等于、大于、等于、大于等于、不等于,返回结果为true或者false
//		System.out.println(a>b);
//		System.out.println(c>b);
		//逻辑运算符：逻辑运算符包括 &&、||、!
//		System.out.println((a>b)&(b>c));//当两边都是true时，返回true，只要有一个false则结果返回false
//		System.out.println((a>b)&&(b>c));//具有短路的效果如果第一个表达式为 false，则不再计算第二个表达式
//		System.out.println((a>b)|(b>c));//|”：前后两个操作数都会进行计算。也就是说：“|”不存在短路
//		System.out.println((a>b)||(b>c));//具有短路的效果||表示短路或，当运算符左边的值为true时，右边的表达式不会进行运算
//		System.out.println(!(a>b));
		//赋值运算符：基本的赋值运算符是“=”。他的优先级别低于其他的运算符，所以对该运算符往往最后读取；+=，-=，*=，/=，%=平时接触这种最多
		a+=1;//a=a+1
//		System.out.println(a);
//		System.out.println(a-=1);
//		System.out.println(a*=1);
//		System.out.println(a/=1);
//		System.out.println(a%=1);
		//条件运算符:三目运算符A?B:C,A,B,C依次为表达式，A是条件表达式，结果为boolean型，如果为true执行B表达式，否则执行C表达式
		System.out.println((a>b?"大于":"小于"));
		System.out.println(a>b?++a:--a);
		
	}
}
