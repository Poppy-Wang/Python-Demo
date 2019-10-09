package lesson1;
//java三大特性：封装，继承，多态
/*封装：通过函数将一些代码封装起来防止外界代码随机访问，要访问这些数据必须通过调用函数；提高了代码的阅读性和可维护性
* 继承：提高代码的复用性和维护性
* public class 父类(){
* }
* public class 子类 extends 父类(){
* }
* 子类可以继承父类的公有属性和方法，子类可以定义父类没有的方法或者通过覆盖父类的方法来扩展
* 
* */
public class Encapsulation {
	public static void main(String[] args) {
		Student student1=new Student();
		//给学生赋值一个年龄
		student1.setAge(29);
		Student student2=new Student();
		//给学生赋值一个年龄
		student2.setAge(28);
		Student student3=new Student();
		//给学生赋值一个年龄
		student3.setAge(27);
	}
}
