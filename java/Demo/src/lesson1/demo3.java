package lesson1;

public class demo3 {
	public static void main(String[] args) {
		//��������ࣺ�������������ϵ��������߼����������ֵ����������������
		int a=1;
		int b=2;
		int c=4;
		//���������
//		System.out.println(a+b);
//		System.out.println(a-b);
//		System.out.println(a*b);
//		System.out.println(a/b);
//		System.out.println(a%b);//ȡ����
//		int aa=a++;
//		int bb=++a;
//		System.out.println(aa);
//		System.out.println(bb);
		//��ϵ��������ֱ�ΪС�ڡ�С�ڵ��ڡ����ڡ����ڡ����ڵ��ڡ�������,���ؽ��Ϊtrue����false
//		System.out.println(a>b);
//		System.out.println(c>b);
		//�߼���������߼���������� &&��||��!
//		System.out.println((a>b)&(b>c));//�����߶���trueʱ������true��ֻҪ��һ��false��������false
//		System.out.println((a>b)&&(b>c));//���ж�·��Ч�������һ�����ʽΪ false�����ټ���ڶ������ʽ
//		System.out.println((a>b)|(b>c));//|����ǰ������������������м��㡣Ҳ����˵����|�������ڶ�·
//		System.out.println((a>b)||(b>c));//���ж�·��Ч��||��ʾ��·�򣬵��������ߵ�ֵΪtrueʱ���ұߵı��ʽ�����������
//		System.out.println(!(a>b));
		//��ֵ������������ĸ�ֵ������ǡ�=�����������ȼ����������������������ԶԸ��������������ȡ��+=��-=��*=��/=��%=ƽʱ�Ӵ��������
		a+=1;//a=a+1
//		System.out.println(a);
//		System.out.println(a-=1);
//		System.out.println(a*=1);
//		System.out.println(a/=1);
//		System.out.println(a%=1);
		//���������:��Ŀ�����A?B:C,A,B,C����Ϊ���ʽ��A���������ʽ�����Ϊboolean�ͣ����Ϊtrueִ��B���ʽ������ִ��C���ʽ
		System.out.println((a>b?"����":"С��"));
		System.out.println(a>b?++a:--a);
		
	}
}
