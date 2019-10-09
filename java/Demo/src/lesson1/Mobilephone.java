package lesson1;
//函数调用方式：15
/*构造函数调用：通常只有在一种情况下才会去调用构造函数，那就是创建对象
 * 非构造函数（普通函数）的调用：需要用到对象来调用，用对象调用普通函数：mobile.sendBrand("小米");
 * 
 * 多态：用父类的类型来接收子类的对象
 * 先决条件：1.继承；2.父类类型接受子类对象
 * 
 * */
public class Mobilephone{
	//全局变量也是类的成员变量
	//品牌
	public String brand;
	//产品类型
	public String generation;
	//价格
	public int price;
	//定义发短信函数,不用返回任何信息
	public void sendMessage(String name){
		System.out.println(name+"晚上一起吃饭");//要发送短信给谁必须要传入一个参数姓名
		System.out.println("此短信通过"+this.brand+this.generation+"手机发出");
	}
	public void call() {
		System.out.println("say hi");
	}
	//给手机设置品牌
	public void setBrand(String brand){
		this.brand=brand;
	}
	//给手机设置型号
	public void setGeneration(String generation){
		this.generation=generation;
	}	
	//给手机设置价格
	public void setPrice(int price){
		this.price=price;
	}	
	//获取手机品牌
	public String getBrand(){
		return this.brand;
	}
    //获取手机型号
	public String getGeneration(){
		return this.generation;
	}
    //获取手机价格
	public int getPrice(){
		return this.price;
	}
	
	public Mobilephone(){//创建类的时候已经，若没有创造构造函数，则默认创造无参构造函数，即使未定义，用户也可以创造原始对象
	//若类中有构造函数，那么默认的无参构造函数就会被覆盖，此时若要通过无参构造函数创建类对象就会报错	
	//无参构造函数只是创造一个原始对象，即默认构造函数，默认的参数即设定的全局参数，为空
	}

	//有参构造函数，通过带参构造函数创造用户想要的对象，需要用户手动创造
	public Mobilephone(String brand,String generation,int price){//三个参数为局部变量,形参
		//把传进来的值传给手机对象，初始化手机对象
		this.brand=brand;//第一个brand为全局变量
		this.generation=generation;
		this.price=price;
	}
	
	public static void main(String[] args) {
		//准备发短信,首先要准备一个手机对象(华为P20,价格8888)，通过构造函数创建一个带品牌和型号的手机对象
		Mobilephone mobilephone=new Mobilephone("华为","P20",8888);//调用带参构造函数创建手机对象，实参
		String name="小明";
		mobilephone.sendMessage(name);
		//调用非构造函数时传入的参数要根据函数传入的参数定义
		Mobilephone mobilephone2=new Mobilephone();
		mobilephone2.call();
		String Brand=mobilephone.getBrand();
		System.out.println(Brand);
		Mobilephone mobilephone3=new Mobilephone();
		//给mobilephone3设置一个品牌
		mobilephone3.setBrand("小米");
		//给mobilephone3设置一个型号
		mobilephone3.setGeneration("青春");
		//给mobilephone3设置一个价格
		mobilephone3.setPrice(2000);
		//取mobilephone3的品牌
		String brand3=mobilephone3.getBrand();
		System.out.println(brand3);
		//取mobilephone3的型号
		String generation3=mobilephone3.getGeneration();
		System.out.println(generation3);
		//取mobilephone3的价格
		int price3=mobilephone3.getPrice();
		System.out.println(price3);
		
	}
	//以下三个函数重载了：重载：函数名字一样，参数有区别，分三种情况
		//1.参数列表不一样：参数个数不一样
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
		//2.参数重载：参数个数一样，参数的类型不一样
		public void test1(int a,int b){
			
		}
		public void test1(int a,String b){
			
		}
		//3.重载：参数类型一样，顺序不一样
		public void test2(int a,String b){
			
		}
		public void test3(String a,int b){
			
		}
}
//初始化对象属性的两种选择：1.通过带参的构造函数来初始化对象的属性；2.通过调用属性的set,get方法来初始化对象的属性（模板方法，可以直接生成）
//函数重载：
//函数名一致，参数不一致
//参数的个数不一致，
//参数的类型不一致
//如果参数的个数一样，类型也一致，但是顺序不一样，即不是重载---15——31







