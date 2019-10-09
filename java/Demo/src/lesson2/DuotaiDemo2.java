package lesson2;

public class DuotaiDemo2 {
//所有iphone手机的品牌信息
	public void showMobileBrand(Mobile mobile){
		mobile.brand();
	}
	public static void main(String[] args) {
		DuotaiDemo2 duotaiDemo2=new DuotaiDemo2();
		Iphone4s iphone4s=new Iphone4s();
		duotaiDemo2.showMobileBrand(iphone4s);//必须要创建一个DuotaiDemo对象
		Iphone5s iphone5s=new Iphone5s();
		duotaiDemo2.showMobileBrand(iphone5s);
	}
}
