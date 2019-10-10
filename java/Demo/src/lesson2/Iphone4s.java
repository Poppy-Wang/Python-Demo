package lesson2;
//
//父类,定义公有 的方法供子类去继承使用
//私有的方法和属性子类无法继承，只有父类可以调用
public class Iphone4s extends Mobile{
	public String brand="iPhone 4s";
//	public void makeCall(){
//		System.out.println("打电话");
//	}
//	public void sendMessage(){
//		System.out.println("发短信");
//	}
	//4s特有的属性
	public void passwordUnlock(){
		System.out.println("密码解锁");
	}
	public void brand() {
		System.out.println(this.brand);
	}
	public static void main(String[] args) {
		Mobile iphone4sMobile=new Iphone4s();
		iphone4sMobile.brand();
		//父类有
		//1.子类也有---调用子类的方法
		//2.子类没有---调用父类的方法
		//父类没有
		//1.子类有---报错
	}
}
//多态：用父类的类型来接受子类的对象
//

