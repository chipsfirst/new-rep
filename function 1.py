name = input("����� ���� ���, ��������:")
print(name + ", ��� ���� ����? ������ �������?")
Yes = "��"
No = "���"
answer =input("������ ������ �� ��� ���:")
if answer == Yes:
    char_name =input("�������� ��� ������ ���������:")
    char_race = input("������ ����. �������� ��� ��� ����:")
    char_class = input("������ �����. ��� ����� ���� ����, ���� ��� ��������")
    print("����� ���������� � Dungeons & Dragons, " + char_race + " " + char_class + " " + char_name)
else:
    print("������, ��������!")
print(
    int(input
