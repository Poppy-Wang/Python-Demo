package lesson1;

public class demo4 {
	public static void main(String[] args) {
		/*for ,while ѭ��
		for(����ʽ){
			ѭ����
		}
		*/
//		for (int i = 1; i < 10; i++) {
//			System.out.println(i);//��ӡÿһ��������ֵ
//		}
		//��1-10�ĺ�
//		int result=1+2+3+4+5+6+7+8+9+10;
//		System.out.println(result);
		//��1-100�ĺ�
//		int result1=0;
//		for(int i=1;i<=100;i++){
//			result1+=i;
//		}
//		System.out.println(result1);
		//String [] names={"111","222","333","444","555"};//�ַ�����������
//		for (int i = 0; i < names.length; i++) {
//			System.out.println(names[i]);
//		}
		//��ǿfor ѭ��:fore
//		for(String name:names){//����name�������մ�names������ȡ������ÿһ�����ݣ�names Ϊ���������
//			System.out.println(name);
//		}
//		for (String string : names) {//������ʾ�������ɱ���string
//			System.out.println(string);
//		}
		//ѭ�����ƣ���������ѭ��---continue;��������ѭ��-----break
		//��iΪ3��ʱ����������ѭ��
//		for (int i = 0; i <=5; i++) {
//			if(i==3){
//				continue;//��iΪ3��ʱ������3���ѭ����������һ������i��Ϊ3��ʱ��һֱִ��������
//			}
//			System.out.println(i);
//		}
		//��iΪ3��ʱ����������ѭ��
//		for (int i = 0; i <=5; i++) {
//			//System.out.println(names[i]);//���ս�������names[3]
//			if(i==3){
//				break;//��iΪ3��ʱ����ֹѭ�����ڼ���������
//			}
//			System.out.println(names[i]);//���ս���������names[3]
//		}
		/*whileѭ�����﷨�ṹ
		 do{
		 ѭ����
		 }while(����)
		 ����
		 while(����){
		 ѭ����
		 }
		 */
//		int x=-1;
//		do {
//			System.out.println(x);
//			x++;
//		} while (x>=0&&x<=5);
//		System.out.println("========");
//		System.out.println(x);
//		int x=0;
//		while(x>=0&&x<=5){
//			System.out.println(x);
//			x++;
//		}
//		System.out.println("========");
//		System.out.println(x);
		/*����������䣺switch
		 * if...else
		  switch(����a){
		  	casea:
		  		...
		  		break
		  	caseb:
		  		...
		  		break
		  	default:
		  		...
		  		break
		  }
		 */
//		int month=19;
//		switch (month) {
//		case 1:
//			System.out.println("����");
//			break;
//		case 2:
//			System.out.println("����");
//			break;
//		case 3:
//			System.out.println("����");
//			break;
//		case 4:
//			System.out.println("�ļ�");
//			break;
//		case 5:
//			System.out.println("�ļ�");
//			break;
//		case 6:
//			System.out.println("�ļ�");
//			break;
//		case 7:
//			System.out.println("�＾");
//			break;
//		case 8:
//			System.out.println("�＾");
//			break;
//		case 9:
//			System.out.println("�＾");
//			break;
//		case 10:
//			System.out.println("����");
//			break;
//		case 11:
//			System.out.println("����");
//			break;
//		case 12:
//			System.out.println("����");
//			break;
//		default:
//			System.out.println("û�д��·ݣ��Ǽ���");
//			break;
//		}
		//if...if
		int score=45;
//		if(score>=60){
//			System.out.println("��ϲ�㼰����");
//		}
//		if(score<60){
//			System.out.println("������˼��û�м���");
//		}
		//if...else
//		if(score>=60){
//			System.out.println("��ϲ�㼰����");
//		}else{
//			System.out.println("������˼��û�м���");
//		}
		//if...else if...else
//		if(score>=85){
//			System.out.println("����");
//		}else if(score>=60&&score<=85){
//			System.out.println("��ϲ�㼰����");
//		}else{
//			System.out.println("������˼��û�м���");
//		}
		//��ӡֱ��������
//		for (int i = 1; i <=5; i++) {//���ѭ�����ƴ�ӡ��������
//			//�ڲ�ѭ������ÿ�д�ӡ����*��
//			//��ӡһ�е����ݣ�ÿһ���ϵ����Ǹ���ȡ����iֵ
//			for(int j=1;j<=i;j++){
//				System.out.print("*");
//			}
//			//����
//			System.out.println();
//		}
	//��ӡ�ȱ�������
		for(int k = 0; k<5;k++){//���ѭ�����ƴ�ӡ��������
			for(int m=k+1;m<5;m++){
				System.out.print(" ");
			}
			//��ӡ*��
			for(int n=0;n<=k;n++){
				System.out.print("* ");
			}
			System.out.println();
		}
		
	}
}