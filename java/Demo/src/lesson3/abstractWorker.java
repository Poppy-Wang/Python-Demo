package lesson3;

public abstract class abstractWorker {
	//��������,�������ж�����󷽷�
	//��������Ҳ���Զ�����ͨ��ʵ�ַ���
	public abstract void work();//������󷽷�����Ϊ��������ȥʵ�ֲ��컯������
	//��ʾһ�칤���ճ���������Ϊ
	public void showDairly(abstractWorker abstractworker){
		System.out.println("��");
		System.out.println("�ϰ�");
		work();
		System.out.println("�°�");
		System.out.println("˯��");
	}
}
