package lesson1;
//java�������ԣ���װ���̳У���̬
/*��װ��ͨ��������һЩ�����װ������ֹ������������ʣ�Ҫ������Щ���ݱ���ͨ�����ú���������˴�����Ķ��ԺͿ�ά����
* �̳У���ߴ���ĸ����Ժ�ά����
* public class ����(){
* }
* public class ���� extends ����(){
* }
* ������Լ̳и���Ĺ������Ժͷ�����������Զ��常��û�еķ�������ͨ�����Ǹ���ķ�������չ
* 
* */
public class Encapsulation {
	public static void main(String[] args) {
		Student student1=new Student();
		//��ѧ����ֵһ������
		student1.setAge(29);
		Student student2=new Student();
		//��ѧ����ֵһ������
		student2.setAge(28);
		Student student3=new Student();
		//��ѧ����ֵһ������
		student3.setAge(27);
	}
}
