package lesson1;
//
public class mobile {
	public String brand;//Ʒ��
	public int price;//�۸�
	//�ֻ����ܣ��ǹ��캯��
	public void sendMessage(String name){
		System.out.println(name+"���ڼ���");
		System.out.print("����Ʒ��"+brand+","+"�۸�"+price+"���ֻ�");
	}
	public String getMobileinfo(){
		return "�ֻ�Ʒ����"+this.brand+","+"�۸���"+this.price;
	}
	//���캯�����������ĺ������޲λ����в�
	/*�޲Σ����η�+������(){}
	 * Public member(){}
	 * �����������η�+������(�������� ������){}
	 * public member(String username,String password){}
	 * 
	 * ע�⣺����Ҫ��ʾ���������������ͣ�����������Ҫ����������һ��
	 * */
	//���캯��
	public mobile(){//�޲Σ�����һ����ԭʼ����
		
	}
	public mobile(String brand,int price){//����,������Ը��ʼ������
		this.brand=brand;//this����һ�����������
		this.price=price;
	}
	public static void main(String[] args) {
		//ͨ���޲ι��캯������һ��ԭʼ����
		mobile mobile1=new mobile();
		//����һ�����ι��캯��������һ������
		mobile mobile2=new mobile("��Ϊ", 2000);
		//��ʾ�ֻ�1Ʒ����Ϣ�ͼ۸���Ϣ
		String info1=mobile1.getMobileinfo();
		System.out.println(info1);
		//��ʾ�ֻ�2Ʒ����Ϣ�ͼ۸���Ϣ
		String info2=mobile2.getMobileinfo();
		System.out.println(info2);
		mobile2.sendMessage("�Ʒ�");
	}
}