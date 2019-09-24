package lesson1;
//
public class mobile {
	public String brand;//品牌
	public int price;//价格
	//手机功能，非构造函数
	public void sendMessage(String name){
		System.out.println(name+"你在家吗");
		System.out.print("发自品牌"+brand+","+"价格"+price+"的手机");
	}
	public String getMobileinfo(){
		return "手机品牌是"+this.brand+","+"价格是"+this.price;
	}
	//构造函数：构造对象的函数，无参或者有参
	/*无参：修饰符+函数名(){}
	 * Public member(){}
	 * 带参数：修饰符+函数名(参数类型 参数名){}
	 * public member(String username,String password){}
	 * 
	 * 注意：不需要显示声明函数返回类型，函数名必须要和类名保持一致
	 * */
	//构造函数
	public mobile(){//无参，创建一个最原始对象
		
	}
	public mobile(String brand,int price){//带参,按照意愿初始化对象
		this.brand=brand;//this代表一个对象的引用
		this.price=price;
	}
	public static void main(String[] args) {
		//通过无参构造函数创造一个原始对象
		mobile mobile1=new mobile();
		//调用一个带参构造函数，创建一个对象
		mobile mobile2=new mobile("华为", 2000);
		//显示手机1品牌信息和价格信息
		String info1=mobile1.getMobileinfo();
		System.out.println(info1);
		//显示手机2品牌信息和价格信息
		String info2=mobile2.getMobileinfo();
		System.out.println(info2);
		mobile2.sendMessage("菲菲");
	}
}
