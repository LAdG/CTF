// Signer.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <math.h>
#include <iostream>
#include <fstream>

using namespace std;

int asciiTOint(char x)
{
	long long int f=0;
	if (x==' ')
	{
	f=1;
	}
	if (x=='!')
	{
		f=2;
	}
	if (x=='"')
	{
		f=3;
	}	
	if (x=='#')
	{
		f=4;
	}	
	if (x=='$')
	{
		f=5;
	}	
	if (x=='%')
	{
		f=6;
	}	
	if (x=='&')
	{
		f=7;
	}	
	if (x=='(')
	{
		f=8;
	}	
	if (x==')')
	{
		f=9;
	}	
	if (x=='*')
	{
		f=10;
	}	
	if (x=='+')
	{
		f=11;
	}	
	if (x==',')
	{
		f=12;
	}	
	if (x=='-')
	{
		f=13;
	}	
	if (x=='.')
	{
		f=14;
	}	
	if (x=='/')
	{
		f=15;
	}	
	if (x=='0')
	{
		f=16;
	}	
	if (x=='1')
	{
		f=17;
	}	
	if (x=='2')
	{
		f=18;
	}	
	if (x=='3')
	{
		f=19;
	}	
	if (x=='4')
	{
		f=20;
	}	
	if (x=='5')
	{
		f=21;
	}	
	if (x=='6')
	{
		f=22;
	}	
	if (x=='7')
	{
		f=23;
	}	
	if (x=='8')
	{
		f=24;
	}	
	if (x=='9')
	{
		f=25;
	}	
	if (x==':')
	{
		f=26;
	}	
	if (x==';')
	{
		f=27;
	}	
	if (x=='<')
	{
		f=28;
	}	
	if (x=='=')
	{
		f=29;
	}	
	if (x=='>')
	{
		f=30;
	}	
	if (x=='?')
	{
		f=31;
	}	
	if (x=='@')
	{
		f=32;
	}	
	if (x=='A')
	{
		f=33;
	}	
	if (x=='B')
	{
		f=34;
	}	
	if (x=='C')
	{
		f=35;
	}	
	if (x=='D')
	{
		f=36;
	}	
	if (x=='E')
	{
		f=37;
	}	
	if (x=='F')
	{
		f=38;
	}	
	if (x=='G')
	{
		f=39;
	}	
	if (x=='H')
	{
		f=40;
	}	
	if (x=='I')
	{
		f=41;
	}	
	if (x=='J')
	{
		f=42;
	}	
	if (x=='K')
	{
		f=43;
	}	
	if (x=='L')
	{
		f=44;
	}	
	if (x=='M')
	{
		f=45;
	}	
	if (x=='N')
	{
		f=46;
	}	
	if (x=='O')
	{
		f=47;
	}	
	if (x=='P')
	{
		f=48;
	}	
	if (x=='Q')
	{
		f=49;
	}	
	if (x=='R')
	{
		f=50;
	}	
	if (x=='S')
	{
		f=51;
	}	
	if (x=='T')
	{
		f=52;
	}	
	if (x=='U')
	{
		f=53;
	}	
	if (x=='V')
	{
		f=54;
	}	
	if (x=='W')
	{
		f=55;
	}	
	if (x=='X')
	{
		f=56;
	}	
	if (x=='Y')
	{
		f=57;
	}	
	if (x=='Z')
	{
		f=58;
	}	
	if (x=='[')
	{
		f=59;
	}	
	if (x==']')
	{
		f=60;
	}	
	if (x=='^')
	{
		f=61;
	}	
	if (x=='_')
	{
		f=62;
	}	
	if (x=='`')
	{
		f=63;
	}	
	if (x=='a')
	{
		f=64;
	}	
	if (x=='b')
	{
		f=65;
	}	
	if (x=='c')
	{
		f=66;
	}	
	if (x=='d')
	{
		f=67;
	}	
	if (x=='e')
	{
		f=68;
	}	
	if (x=='f')
	{
		f=69;
	}	
	if (x=='g')
	{
		f=70;
	}	
	if (x=='h')
	{
		f=71;
	}	
	if (x=='i')
	{
		f=72;
	}	
	if (x=='j')
	{
		f=73;
	}	
	if (x=='k')
	{
		f=74;
	}	
	if (x=='l')
	{
		f=75;
	}	
	if (x=='m')
	{
		f=76;
	}	
	if (x=='n')
	{
		f=77;
	}	
	if (x=='o')
	{
		f=78;
	}	
	if (x=='p')
	{
		f=79;
	}	
	if (x=='q')
	{
		f=80;
	}	
	if (x=='r')
	{
		f=81;
	}	
	if (x=='s')
	{
		f=82;
	}	
	if (x=='t')
	{
		f=83;
	}	
	if (x=='u')
	{
		f=84;
	}	
	if (x=='v')
	{
		f=85;
	}	
	if (x=='w')
	{
		f=86;
	}	
	if (x=='x')
	{
		f=87;
	}	
	if (x=='y')
	{
		f=88;
	}	
	if (x=='z')
	{
		f=89;
	}	
	if (x=='{')
	{
		f=90;
	}	
	if (x=='|')
	{
		f=91;
	}	
	if (x=='}')
	{
		f=92;
	}	
	if (x=='~')
	{
		f=93;
	}	
	if (x=='Ђ')
	{
		f=94;
	}	
	if (x=='Ѓ')
	{
		f=95;
	}	
	if (x=='ѓ')
	{
		f=96;
	}	
	if (x=='„')
	{
		f=97;
	}	
	if (x=='…')
	{
		f=98;
	}	
	if (x=='†')
	{
		f=99;
	}
	if (x=='‡')
	{
		f=100;
	}
	if (x=='€')
	{
		f=101;
	}	
	if (x=='‰')
	{
		f=102;
	}	
	if (x=='Љ')
	{
		f=103;
	}	
	if (x=='‹')
	{
		f=104;
	}	
	if (x=='Њ')
	{
		f=105;
	}	
	if (x=='Ќ')
	{
		f=106;
	}	
	if (x=='Ћ')
	{
		f=107;
	}	
	if (x=='Џ')
	{
		f=108;
	}	
	if (x=='ђ')
	{
		f=109;
	}	
	if (x=='‘')
	{
		f=110;
	}	
	if (x=='’')
	{
		f=111;
	}	
	if (x=='“')
	{
		f=112;
	}	
	if (x=='”')
	{
		f=113;
	}	
	if (x=='•')
	{
		f=114;
	}	
	if (x=='–')
	{
		f=115;
	}	
	if (x=='—')
	{
		f=116;
	}	
	if (x=='�')
	{
		f=117;
	}	
	if (x=='™')
	{
		f=118;
	}	
	if (x=='љ')
	{
		f=119;
	}	
	if (x=='›')
	{
		f=120;
	}	
	if (x=='њ')
	{
		f=121;
	}	
	if (x=='ќ')
	{
		f=122;
	}	
	if (x=='ћ')
	{
		f=123;
	}	
	if (x=='џ')
	{
		f=124;
	}	
	if (x=='Ў')
	{
		f=125;
	}	
	if (x=='ў')
	{
		f=126;
	}	
	if (x=='¤')
	{
		f=127;
	}	
	if (x=='Ґ')
	{
		f=128;
	}	
	if (x=='¦')
	{
		f=129;
	}	
	if (x=='§')
	{
		f=130;
	}	
	if (x=='Ё')
	{
		f=131;
	}	
	if (x=='©')
	{
		f=132;
	}	
	if (x=='Є')
	{
		f=133;
	}	
	if (x=='«')
	{
		f=134;
	}	
	if (x=='¬')
	{
		f=135;
	}	
	if (x=='®')
	{
		f=136;
	}	
	if (x=='Ї')
	{
		f=137;
	}	
	if (x=='°')
	{
		f=138;
	}	
	if (x=='±')
	{
		f=139;
	}	
	if (x=='ґ')
	{
		f=140;
	}	 
	if (x=='µ')
	{
		f=141;
	}	
	if (x=='¶')
	{
		f=142;
	}	
	if (x=='·')
	{
		f=143;
	}	
	if (x=='ё')
	{
		f=144;
	}	
	if (x=='№')
	{
		f=145;
	}	
	if (x=='є')
	{
		f=146;
	}	
	if (x=='»')
	{
		f=147;
	}	
	if (x=='ї')
	{
		f=148;
	}	
	if (x=='А')
	{
		f=149;
	}	
	if (x=='Б')
	{
		f=150;
	}	
	if (x=='В')
	{
		f=151;
	}	
	if (x=='Г')
	{
		f=152;
	}	
	if (x=='Д')
	{
		f=153;
	}	
	if (x=='Е')
	{
		f=154;
	}	
	if (x=='Ж')
	{
		f=155;
	}	
	if (x=='З')
	{
		f=156;
	}	
	if (x=='И')
	{
		f=157;
	}	
	if (x=='Й')
	{
		f=158;
	}	
	if (x=='К')
	{
		f=159;
	}	
	if (x=='Л')
	{
		f=160;
	}	
	if (x=='М')
	{
		f=161;
	}	
	if (x=='Н')
	{
		f=162;
	}	
	if (x=='О')
	{
		f=163;
	}	
	if (x=='П')
	{
		f=164;
	}	
	if (x=='Р')
	{
		f=165;
	}	
	if (x=='С')
	{
		f=166;
	}	
	if (x=='Т')
	{
		f=167;
	}	
	if (x=='У')
	{
		f=168;
	}	
	if (x=='Ф')
	{
		f=169;
	}	
	if (x=='Х')
	{
		f=170;
	}	
	if (x=='Ц')
	{
		f=171;
	}	
	if (x=='Ч')
	{
		f=172;
	}	
	if (x=='Ш')
	{
		f=173;
	}	
	if (x=='Щ')
	{
		f=174;
	}	
	if (x=='Ъ')
	{
		f=175;
	}	
	if (x=='Ы')
	{
		f=176;
	}	
	if (x=='Ь')
	{
		f=177;
	}	
	if (x=='Э')
	{
		f=178;
	}	
	if (x=='Ю')
	{
		f=179;
	}	
	if (x=='Я')
	{
		f=180;
	}	
	if (x=='а')
	{
		f=181;
	}	
	if (x=='б')
	{
		f=182;
	}	
	if (x=='в')
	{
		f=183;
	}	
	if (x=='г')
	{
		f=184;
	}	
	if (x=='д')
	{
		f=185;
	}	
	if (x=='е')
	{
		f=186;
	}	
	if (x=='ж')
	{
		f=187;
	}	
	if (x=='з')
	{
		f=188;
	}	
	if (x=='и')
	{
		f=189;
	}	
	if (x=='й')
	{
		f=190;
	}	
	if (x=='к')
	{
		f=191;
	}	
	if (x=='л')
	{
		f=192;
	}	
	if (x=='м')
	{
		f=193;
	}	
	if (x=='н')
	{
		f=194;
	}	
	if (x=='о')
	{
		f=195;
	}	
	if (x=='п')
	{
		f=196;
	}	
	if (x=='р')
	{
		f=197;
	}
	if (x=='с')
	{
		f=198;
	}
	if (x=='т')
	{
		f=199;
	}
	if (x=='у')
	{
		f=200;
	}
	if (x=='ф')
	{
		f=201;
	}
	if (x=='х')
	{
		f=202;
	}
	if (x=='ц')
	{
		f=203;
	}
	if (x=='ч')
	{
		f=204;
	}
	if (x=='ш')
	{
		f=205;
	}
	if (x=='щ')
	{
		f=206;
	}
	if (x=='ъ')
	{
		f=207;
	}
	if (x=='ы')
	{
		f=208;
	}
	if (x=='ь')
	{
		f=209;
	}
	if (x=='э')
	{
		f=210;
	}
	if (x=='ю')
	{
		f=211;
	}
	if (x=='я')
	{
		f=212;
	}
	return f;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int count=0, i;
	long long int a=0, b=1, k, p=2000053603;
	char ch;
	char buf[10000];
	long long int A[10000];
	cout<< "Enter key for sign:\n";
	cin>>k;
	ifstream in("Contract.txt");
	ofstream out;
	while (in.get(ch))
	{ 		
		count++;
	}
	in.clear();
	in.seekg(0, ios::beg);
	in.getline(buf,count);	
	i=0;
	count=count-1;
	while (i<count)
	{
	A[i]=asciiTOint(buf[i]);
	a=a+A[i];
	i++;
	}
	in.close();
	i=0;
	while (i<k)
	{
	b=(b*a)%p;
	i++;
	}
	out.open("Sign.sgn");
	out << b;
	out.close();
	cin.get();
	cin.get();
	return 0;
}
