package lesson2;
//
//����,���幫�� �ķ���������ȥ�̳�ʹ��
//˽�еķ��������������޷��̳У�ֻ�и�����Ե���
public class Iphone4s extends Mobile{
	public String brand="iPhone 4s";
//	public void makeCall(){
//		System.out.println("��绰");
//	}
//	public void sendMessage(){
//		System.out.println("������");
//	}
	//4s���е�����
	public void passwordUnlock(){
		System.out.println("�������");
	}
	public void brand() {
		System.out.println(this.brand);
	}
	public static void main(String[] args) {
		Mobile iphone4sMobile=new Iphone4s();
		iphone4sMobile.brand();
		//������
		//1.����Ҳ��---��������ķ���
		//2.����û��---���ø���ķ���
		//����û��
		//1.������---����
	}
}
//��̬���ø������������������Ķ���
//

