package lesson3;

public interface worker {
//工作：抽象的方法(未实现的方法),接口里默认方法就是public abstract类型
	public abstract void work();
	//接口里面定义变量都是static final类型，final类型不可修改，即常量,接口里默认的数据类型就是static final
	//接口里面不能实例化，接口可以多继承，interface worker extends A,B,C,类不可以多继承
	public static final String title="工人";
}
//接口解决的问题：类型耦合，代码的可维护，
