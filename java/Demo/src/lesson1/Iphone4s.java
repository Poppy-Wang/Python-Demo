package lesson1;
//
//父类,定义公有 的方法供子类去继承使用
//私有的方法和属性子类无法继承，只有父类可以调用
public class Iphone4s {
	public String brand="iPhone 4s";
	public void makeCall(){
		System.out.println("打电话");
	}
	public void sendMessage(){
		System.out.println("发短信");
	}
	public void passwordUnlock(){
		System.out.println("密码解锁");
	}
	public void test(){
		//父类的测试方法
		System.out.println("父类的测试方法");
	}
}
//多态：用父类的类型来接受子类的对象
//
