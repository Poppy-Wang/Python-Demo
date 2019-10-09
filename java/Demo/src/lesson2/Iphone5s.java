package lesson2;

public class Iphone5s extends Iphone5{
	public String brand="iPhone 5s";//属性覆盖
//	public static void main(String[] args) {
//		Iphone5s iphone5s=new Iphone5s();
//		iphone5s.passwordUnlock();
//		//仍然可以访问，因为继承具有传递性，Iphone5继承了Iphone4s，Iphone5s继承了Iphone5，所有也同样具有
//		//Iphone4s公有的属性和方法
//	}
	public void fingerUnlock(){
		System.out.println("指纹解锁");
	}
	public void brand() {
		System.out.println(this.brand);
	}
}
