package lesson2;

public class DuotaiDemo {
	//���Iphone4s�ֻ�Ʒ����Ϣ
	public void showIphone4sBrand(Iphone4s iphone4s){
		iphone4s.brand();
	}
	//���Iphone5�ֻ�Ʒ����Ϣ
		public void showIphone5Brand(Iphone5 iphone5){
			iphone5.brand();
		}
		//���Iphone5s�ֻ�Ʒ����Ϣ
		public void showIphone5sBrand(Iphone5s iphone5s){
			iphone5s.brand();
		}
		//���Iphone6�ֻ�Ʒ����Ϣ
		public void showIphone6Brand(Iphone6 iphone6){
			iphone6.brand();
		}
		public static void main(String[] args) {
			DuotaiDemo duotaiDemo=new DuotaiDemo();
			Iphone4s iphone4s=new Iphone4s();
			duotaiDemo.showIphone4sBrand(iphone4s);//����Ҫ����һ��DuotaiDemo����
		}
}
