package lesson2;

public class DuotaiDemo {
	//输出Iphone4s手机品牌信息
	public void showIphone4sBrand(Iphone4s iphone4s){
		iphone4s.brand();
	}
	//输出Iphone5手机品牌信息
		public void showIphone5Brand(Iphone5 iphone5){
			iphone5.brand();
		}
		//输出Iphone5s手机品牌信息
		public void showIphone5sBrand(Iphone5s iphone5s){
			iphone5s.brand();
		}
		//输出Iphone6手机品牌信息
		public void showIphone6Brand(Iphone6 iphone6){
			iphone6.brand();
		}
		public static void main(String[] args) {
			DuotaiDemo duotaiDemo=new DuotaiDemo();
			Iphone4s iphone4s=new Iphone4s();
			duotaiDemo.showIphone4sBrand(iphone4s);//必须要创建一个DuotaiDemo对象
		}
}
