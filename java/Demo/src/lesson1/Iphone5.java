package lesson1;

public class Iphone5 extends Iphone4s{
	public String brand="iPhone 5";//属性覆盖
	public static void main(String[] args) {
		//用Iphone5发短信
		Iphone5 iphone5=new Iphone5();
		iphone5.sendMessage();
		iphone5.test();
		System.out.println(iphone5.brand);//子类可以继承父类公共的属性和方法
	}
	public void test(){
		//super.test();super表示父类对象的调用，this表示当前对象的引用
		System.out.println("子类的测试方法");
	}
}
