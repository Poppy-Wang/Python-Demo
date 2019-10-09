package lesson2;

public class Mobile {
	public String brand="未知品牌的手机";
	public void makeCall(){
		System.out.println("打电话");
	}
	public void sendMessage(){
		System.out.println("发短信");
	}
//	public void passwordUnlock(){
//		System.out.println("密码解锁");
//	}
	public void brand() {
		System.out.println(this.brand);
	}
}
