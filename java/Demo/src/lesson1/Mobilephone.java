package lesson1;
//�������÷�ʽ��15
/*���캯�����ã�ͨ��ֻ����һ������²Ż�ȥ���ù��캯�����Ǿ��Ǵ�������
 * �ǹ��캯������ͨ�������ĵ��ã���Ҫ�õ����������ã��ö��������ͨ������mobile.sendBrand("С��");
 * 
 * ��̬���ø������������������Ķ���
 * �Ⱦ�������1.�̳У�2.�������ͽ����������
 * 
 * */
public class Mobilephone{
	//ȫ�ֱ���Ҳ����ĳ�Ա����
	//Ʒ��
	public String brand;
	//��Ʒ����
	public String generation;
	//�۸�
	public int price;
	//���巢���ź���,���÷����κ���Ϣ
	public void sendMessage(String name){
		System.out.println(name+"����һ��Է�");//Ҫ���Ͷ��Ÿ�˭����Ҫ����һ����������
		System.out.println("�˶���ͨ��"+this.brand+this.generation+"�ֻ�����");
	}
	public void call() {
		System.out.println("say hi");
	}
	//���ֻ�����Ʒ��
	public void setBrand(String brand){
		this.brand=brand;
	}
	//���ֻ������ͺ�
	public void setGeneration(String generation){
		this.generation=generation;
	}	
	//���ֻ����ü۸�
	public void setPrice(int price){
		this.price=price;
	}	
	//��ȡ�ֻ�Ʒ��
	public String getBrand(){
		return this.brand;
	}
    //��ȡ�ֻ��ͺ�
	public String getGeneration(){
		return this.generation;
	}
    //��ȡ�ֻ��۸�
	public int getPrice(){
		return this.price;
	}
	
	public Mobilephone(){//�������ʱ���Ѿ�����û�д��칹�캯������Ĭ�ϴ����޲ι��캯������ʹδ���壬�û�Ҳ���Դ���ԭʼ����
	//�������й��캯������ôĬ�ϵ��޲ι��캯���ͻᱻ���ǣ���ʱ��Ҫͨ���޲ι��캯�����������ͻᱨ��	
	//�޲ι��캯��ֻ�Ǵ���һ��ԭʼ���󣬼�Ĭ�Ϲ��캯����Ĭ�ϵĲ������趨��ȫ�ֲ�����Ϊ��
	}

	//�вι��캯����ͨ�����ι��캯�������û���Ҫ�Ķ�����Ҫ�û��ֶ�����
	public Mobilephone(String brand,String generation,int price){//��������Ϊ�ֲ�����,�β�
		//�Ѵ�������ֵ�����ֻ����󣬳�ʼ���ֻ�����
		this.brand=brand;//��һ��brandΪȫ�ֱ���
		this.generation=generation;
		this.price=price;
	}
	
	public static void main(String[] args) {
		//׼��������,����Ҫ׼��һ���ֻ�����(��ΪP20,�۸�8888)��ͨ�����캯������һ����Ʒ�ƺ��ͺŵ��ֻ�����
		Mobilephone mobilephone=new Mobilephone("��Ϊ","P20",8888);//���ô��ι��캯�������ֻ�����ʵ��
		String name="С��";
		mobilephone.sendMessage(name);
		//���÷ǹ��캯��ʱ����Ĳ���Ҫ���ݺ�������Ĳ�������
		Mobilephone mobilephone2=new Mobilephone();
		mobilephone2.call();
		String Brand=mobilephone.getBrand();
		System.out.println(Brand);
		Mobilephone mobilephone3=new Mobilephone();
		//��mobilephone3����һ��Ʒ��
		mobilephone3.setBrand("С��");
		//��mobilephone3����һ���ͺ�
		mobilephone3.setGeneration("�ഺ");
		//��mobilephone3����һ���۸�
		mobilephone3.setPrice(2000);
		//ȡmobilephone3��Ʒ��
		String brand3=mobilephone3.getBrand();
		System.out.println(brand3);
		//ȡmobilephone3���ͺ�
		String generation3=mobilephone3.getGeneration();
		System.out.println(generation3);
		//ȡmobilephone3�ļ۸�
		int price3=mobilephone3.getPrice();
		System.out.println(price3);
		
	}
	//�����������������ˣ����أ���������һ�������������𣬷��������
		//1.�����б�һ��������������һ��
		public void setMobileinfo(String brand){
			this.brand=brand;
		}
		public void setMobileinfo(String brand,String generation){
			this.brand=brand;
			this.generation=generation;
		}
		public void setMobileinfo(String brand,String generation,int price){
			this.brand=brand;
			this.generation=generation;
			this.price=price;
		}
		//2.�������أ���������һ�������������Ͳ�һ��
		public void test1(int a,int b){
			
		}
		public void test1(int a,String b){
			
		}
		//3.���أ���������һ����˳��һ��
		public void test2(int a,String b){
			
		}
		public void test3(String a,int b){
			
		}
}
//��ʼ���������Ե�����ѡ��1.ͨ�����εĹ��캯������ʼ����������ԣ�2.ͨ���������Ե�set,get��������ʼ����������ԣ�ģ�巽��������ֱ�����ɣ�
//�������أ�
//������һ�£�������һ��
//�����ĸ�����һ�£�
//���������Ͳ�һ��
//��������ĸ���һ��������Ҳһ�£�����˳��һ��������������---15����31







