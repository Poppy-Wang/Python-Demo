package lesson1;

public class Iphone6 extends Iphone4s{
	public String brand="iPhone6";//属性覆盖
	public static void main(String[] args) {
		Iphone6 iphone6=new Iphone6();
		iphone6.makeCall();
	}
	public void shape(){
		System.out.println("Iphone6特有的");
	}
	@Override//覆盖父类的方法
	public void test() {
		System.out.println("子类test测试方法");
	}
}
