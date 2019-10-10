package lesson3;
//实现类
//public class Teacher implements worker{
public class Teacher extends abstractWorker{
//实现接口就要强制的实现接口里定义的方法
	@Override
	public void work() {
		// TODO Auto-generated method stub
		System.out.println("教书");
	}

	//public void test();类中不可以定义抽象方法，抽象类里可以定义抽象方法
}
