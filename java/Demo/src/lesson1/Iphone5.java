package lesson1;

public class Iphone5 extends Iphone4s{
	public String brand="iPhone 5";//���Ը���
	public static void main(String[] args) {
		//��Iphone5������
		Iphone5 iphone5=new Iphone5();
		iphone5.sendMessage();
		iphone5.test();
		System.out.println(iphone5.brand);//������Լ̳и��๫�������Ժͷ���
	}
	public void test(){
		//super.test();super��ʾ�������ĵ��ã�this��ʾ��ǰ���������
		System.out.println("����Ĳ��Է���");
	}
}
