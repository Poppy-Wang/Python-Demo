package lesson3;

public abstract class abstractWorker {
	//工作方法,抽象类中定义抽象方法
	//抽象类中也可以定义普通的实现方法
	public abstract void work();//定义抽象方法就是为了让子类去实现差异化的内容
	//显示一天工作日常，公共行为
	public void showDairly(abstractWorker abstractworker){
		System.out.println("起床");
		System.out.println("上班");
		work();
		System.out.println("下班");
		System.out.println("睡觉");
	}
}
